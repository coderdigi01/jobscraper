from django.core.management.base import BaseCommand
from jobs.scraper import scrape_jobs
from jobs.google_sheets import update_sheet

class Command(BaseCommand):
    help = "Scrape jobs, save in DB, and update Google Sheets"

    def handle(self, *args, **kwargs):
        self.stdout.write("Scraping jobs...")
        jobs = scrape_jobs()
        update_sheet(jobs)
        self.stdout.write(self.style.SUCCESS("✅ Jobs saved in DB and updated in Google Sheets!"))
