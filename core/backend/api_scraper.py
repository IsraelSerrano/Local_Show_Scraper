import sqlite3
from apify_client import ApifyClient
from dotenv import load_dotenv
import os


def api_scrape_profiles(usernames):
    load_dotenv()

    # Initialize the ApifyClient with your API token
    client = ApifyClient(os.getenv("APIFY_KEY"))

    direct_urls = [f"https://www.instagram.com/{username}/" for username in usernames]

    # List of Instagram post URLs to scrape
    # Prepare the Actor input
    run_input = {
        "directUrls": direct_urls,
        "resultsType": "posts",  # We want post data
        "resultsLimit": 1,  # Limit results to the number of posts
        "addParentData": False,  # No need for parent data
    }

    # Run the Actor and wait for it to finish
    run = client.actor("shu8hvrXbJbY3Eb9W").call(run_input=run_input)

    # Connect to SQLite database (or create it if it doesn't exist)
    conn = sqlite3.connect("instagram_posts.db")
    cursor = conn.cursor()

    # Create a table if it doesn't already exist
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS posts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT,
            post_url TEXT,
            caption TEXT,
            image_url TEXT,
            alt_image TEXT,
            tagged_users TEXT
        )
    """)

    # Fetch and process results from the dataset
    for item in client.dataset(run["defaultDatasetId"]).iterate_items():
        # Extract the caption and image URL
        username = item.get("ownerUsername", "No username available")
        caption = item.get("caption", "No caption available")
        tagged_users_list = item.get("taggedUsers", [])
        image_url = item.get("displayUrl", "No image URL available")
        alt_image =  item.get("alt", "No image URL available")
        post_url = item.get("url", "No post URL available")

        # Parse tagged users to extract only usernames
        if tagged_users_list:
            tagged_usernames = ", ".join(user["username"] for user in tagged_users_list)
        else:
            tagged_usernames = "No tagged users"

        # Print the results to the console
        print(f"Username: {username}")
        print(f"Post URL: {post_url}")
        print(f"Caption: {caption}")
        print(f"Image URL: {image_url}")
        print(f"Alt Image: {alt_image}")
        print(f"Tagged Users: {tagged_usernames}")
        print("-" * 50)

        # Insert the data into the SQLite database
        cursor.execute("""
            INSERT INTO posts (username, post_url, caption, image_url, alt_image, tagged_users)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (username, post_url, caption, image_url, alt_image, tagged_usernames))

    # Commit changes and close the connection
    conn.commit()
    conn.close()