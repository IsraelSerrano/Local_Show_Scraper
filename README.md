# Local Show ABAC Scraper

This project is aimed to proivde a platform to grab local shows off of social media and store them in a database to proivde a singular place to find all these shows.

## Features

- Scrape Instagram post captions and image metadata using Selenium.
- Download images from Instagram posts.
- Use Apify API for efficient and structured data scraping.
- Save scraped data to text files for further analysis.

## Prerequisites

- Python 3.13 or higher
- Google Chrome browser
- ChromeDriver (compatible with your Chrome version)

## Installation

#### 1. Clone the repository:

```
git clone https://github.com/your-username/Local_Show_Scraper.git
cd Local_Show_Scraper
```

#### 2. (Recommended) Intialize a virtual environment

```
python3 -m venv venv
source venv/bin/activate
```

#### 3. Install Dependencies

```
pip install -r /path/to/requirements.txt
```

#### 4. Set up environment variables:

Create a .env file in the project root and add the following:
&nbsp;&nbsp;&nbsp;&nbsp;INSTAGRAM_USERNAME=your_instagram_username
&nbsp;&nbsp;&nbsp;&nbsp;INSTAGRAM_PASSWORD=your_instagram_password
&nbsp;&nbsp;&nbsp;&nbsp;APIFY_KEY=your_apify_api_key
