# File: web_scraper.py

import requests
from bs4 import BeautifulSoup
import csv

def scrape_jobs(url, output_file):
    """Scrapes job postings from the specified URL and writes them to a CSV file."""
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract job postings (adjust selectors based on the site's structure)
        job_listings = soup.find_all('div', class_='job-card')

        # Open CSV file for writing
        with open(output_file, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Title', 'Company', 'Location', 'Summary'])

            for job in job_listings:
                title = job.find('h2', class_='title').text.strip()
                company = job.find('h3', class_='company').text.strip()
                location = job.find('p', class_='location').text.strip()
                summary = job.find('div', class_='summary').text.strip()
                writer.writerow([title, company, location, summary])

        print(f"Scraped data saved to {output_file}")

    except Exception as e:
        print(f"Error during scraping: {e}")

if __name__ == '__main__':
    target_url = "https://example.com/jobs"  # Replace with the actual job board URL
    output_csv = "job_postings.csv"
    scrape_jobs(target_url, output_csv)
