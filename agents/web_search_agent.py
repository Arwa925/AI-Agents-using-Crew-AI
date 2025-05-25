import random
from utils.scraper import scrape_jobs_from_platforms

class WebSearchAgent:
    def run(self):
        print("[WebSearchAgent] Searching job boards...")
        data = scrape_jobs_from_platforms()
        print(f"[WebSearchAgent] Fetched {len(data)} job postings.")
        return data
