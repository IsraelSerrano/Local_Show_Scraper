from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from dotenv import load_dotenv
import os
import time
import wget

load_dotenv()

def main():
    # test post dictionaries

    posts = {
        "ROSEWOOD_POST_URL" : "https://www.instagram.com/p/DHZ5F1_P5Os/",
        "VIV_POST_URL" : "https://www.instagram.com/p/DGllXgQy4hw/"
    }

    # Set up Selenium WebDriver
    chrome_options = Options()
    # chrome_options.add_argument("--headless")  # Run in headless mode

    driver = webdriver.Chrome(options=chrome_options)

    # login(driver)

    with open("captions.txt", "w", encoding="utf-8") as file:
        for post_url in posts.values():
            post_data = get_post_data(driver, post_url)
            # Write the caption and link to the file
            file.write(f"Post URL: {post_url}\n")
            file.write(f"Caption: {post_data["caption_text"]}\n")
            file.write(f"Image Text: {post_data["image_text"]}\n")
            file.write("-" * 50 + "\n")  # Separator for readability

    driver.quit()

def get_post_data(driver, post_url):
    driver.get(post_url)

    time.sleep(5)
    ActionChains(driver).send_keys(Keys.ESCAPE).perform()
    caption_element = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/section/main/div[2]/div[1]/article/div/div[2]/div/div[2]/div[1]/ul/div[1]/li/div/div/div[2]")

    image = driver.find_element(By.TAG_NAME, "img")

    image_text = image.get_attribute('alt')

    # Extract and print the caption text
    caption_text = caption_element.text
    
    post_data = {"caption_text" : caption_text, "image_text" : image_text}
    
    return post_data


# sign in if necessary
def login(driver):
    # grab credentials
    driver.get("https://www.instagram.com/")
    username_value = os.getenv("INSTAGRAM_USERNAME")
    password_value = os.getenv("INSTAGRAM_PASSWORD")
    
    username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name=username]")))
    password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name=password]")))

    username.clear()
    password.clear()

    username.send_keys(username_value)
    password.send_keys(password_value)
    log_in = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type=submit]"))).click()


if __name__ == '__main__':
    main()