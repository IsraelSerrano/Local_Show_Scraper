from apify_client import ApifyClient
from dotenv import load_dotenv
import os

load_dotenv()

# Initialize the ApifyClient with your API token
client = ApifyClient(os.getenv("APIFY_KEY"))

# List of Instagram post URLs to scrape
post_urls = ["https://www.instagram.com/p/DGUevIzR7E2/", "https://www.instagram.com/p/DHZ5F1_P5Os/"]

# Prepare the Actor input
run_input = {
    "directUrls": post_urls,  # Direct URLs of the Instagram posts
    "resultsType": "posts",  # We want post data
    "resultsLimit": len(post_urls),  # Limit results to the number of posts
    "addParentData": False,  # No need for parent data
}

# Run the Actor and wait for it to finish
run = client.actor("shu8hvrXbJbY3Eb9W").call(run_input=run_input)

# Open a file to save the results
with open("instagram_posts.txt", "w", encoding="utf-8") as file:
    # Fetch and process results from the dataset
    for item in client.dataset(run["defaultDatasetId"]).iterate_items():
        # Extract the caption and image URL
        caption = item.get("caption", "No caption available")
        image_url = item.get("imageUrl", "No image URL available")
        post_url = item.get("url", "No post URL available")

        # Print the results to the console
        print(f"Post URL: {post_url}")
        print(f"Caption: {caption}")
        print(f"Image URL: {image_url}")
        print("-" * 50)

        # Write the results to the file
        file.write(f"Post URL: {post_url}\n")
        file.write(f"Caption: {caption}\n")
        file.write(f"Image URL: {image_url}\n")
        file.write("-" * 50 + "\n")