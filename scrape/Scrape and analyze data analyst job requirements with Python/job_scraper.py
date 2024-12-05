from datetime import datetime
import csv
import requests
from bs4 import BeautifulSoup
import time
import logging
import random
from typing import Dict, List, Optional

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class JobScraper:
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
    
    def generate_linkedin_url(self, position: str, location: str) -> str:
        """Generate LinkedIn URL for job search"""
        position = position.replace(' ', '%20')
        location = location.replace(' ', '%20')
        return f"https://www.linkedin.com/jobs/search?keywords={position}&location={location}"

    def extract_linkedin_job_data(self, job_card: BeautifulSoup) -> Optional[Dict]:
        """Extract job data from a LinkedIn job card"""
        try:
            # Extract basic job information
            title = job_card.find('h3', class_='base-search-card__title').text.strip()
            company = job_card.find('h4', class_='base-search-card__subtitle').text.strip()
            location = job_card.find('span', class_='job-search-card__location').text.strip()
            
            # Extract job link
            job_link = job_card.find('a', class_='base-card__full-link')['href']
            
            # Extract posting date
            date_posted = job_card.find('time')['datetime'] if job_card.find('time') else None
            
            # Get job description from the job detail page
            description = ""
            try:
                # Add delay before requesting job details
                time.sleep(random.uniform(2, 4))
                
                # Make request to job detail page
                job_response = requests.get(job_link, headers=self.headers)
                
                if job_response.status_code == 200:
                    job_soup = BeautifulSoup(job_response.text, 'html.parser')
                    
                    # Find the job description
                    description_div = job_soup.find('div', class_='show-more-less-html__markup')
                    if description_div:
                        description = description_div.get_text(strip=True)
                    else:
                        # Try alternative class names
                        description_div = job_soup.find('div', class_='description__text')
                        if description_div:
                            description = description_div.get_text(strip=True)
                else:
                    logger.warning(f"Could not fetch job description. Status code: {job_response.status_code}")
                    description = "No description available"
            
            except Exception as e:
                logger.warning(f"Error fetching job description: {e}")
                description = "No description available"
            
            # Create job data dictionary
            job_data = {
                'title': title,
                'company': company,
                'location': location,
                'job_link': job_link,
                'date_posted': date_posted,
                'description': description,
                'source': 'LinkedIn',
                'date_scraped': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            
            return job_data
        
        except Exception as e:
            logger.error(f"Error extracting job data: {e}")
            return None

    def scrape_jobs(self, position: str, location: str) -> List[Dict]:
        """Main function to scrape jobs from LinkedIn"""
        all_jobs = []
        
        # Add rotation of user agents
        user_agents = [
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0'
        ]
            
        # Scrape LinkedIn
        linkedin_url = self.generate_linkedin_url(position, location)
        try:
            # Rotate user agents
            self.headers['User-Agent'] = random.choice(user_agents)
            
            # Add delay before request
            time.sleep(random.uniform(2, 5))
            
            response = requests.get(linkedin_url, headers=self.headers)
            
            # Check if we're being blocked
            if response.status_code != 200:
                logger.error(f"LinkedIn returned status code: {response.status_code}")
                return all_jobs
                
            soup = BeautifulSoup(response.content, 'html.parser')
            job_cards = soup.find_all('div', {'class': 'base-card'})
            
            for card in job_cards:
                job_data = self.extract_linkedin_job_data(card)
                if job_data:
                    all_jobs.append(job_data)
                    logger.info(f"Successfully scraped job: {job_data['title']} at {job_data['company']}")
            
            logger.info(f"Successfully scraped {len(all_jobs)} valid jobs from LinkedIn")
            
        except Exception as e:
            logger.error(f"Error occurred while scraping LinkedIn: {e}")
        
        return all_jobs

    def save_to_csv(self, jobs: List[Dict], filename: str):
        """Save job listings to CSV file"""
        if not jobs:
            logger.warning("No jobs to save")
            return
            
        fieldnames = ['title', 'company', 'location', 'job_link', 'date_posted', 'description', 'source', 'date_scraped']
        
        try:
            with open(filename, 'w', newline='', encoding='utf-8') as f:
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(jobs)
            logger.info(f"Successfully saved {len(jobs)} jobs to {filename}")
        except Exception as e:
            logger.error(f"Error saving to CSV: {e}")