from job_scraper import JobScraper
from datetime import datetime
import time
import random

def main():
    scraper = JobScraper()
    
    position = input("Enter job position to search for: ")
    location = input("Enter location: ")
    
    # Add delays between requests
    time.sleep(random.uniform(2, 5))
    
    try:
        jobs = scraper.scrape_jobs(position, location)
        filename = f"job_listings_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
        scraper.save_to_csv(jobs, filename)
    except Exception as e:
        print(f"Error occurred: {e}")
        print("Consider using LinkedIn's official API instead of scraping")

if __name__ == "__main__":
    main() 