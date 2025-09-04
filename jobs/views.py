from .models import Job
from django.shortcuts import render, redirect
from django.contrib import messages
from .scraper import scrape_jobs
from .google_sheets import update_sheet

# Create your views here.

def home(request):
    all_jobs = Job.objects.all().order_by('-created_at')
    context = {"jobs": all_jobs}
    return render(request, "home.html", context)



def run_scraper(request):
    """Run scraper manually with button"""
    jobs = scrape_jobs()  # saves in DB inside scraper
    update_sheet(jobs)    # push to Google Sheets
    messages.success(request, f"✅ Scraped {len(jobs)} jobs and updated Google Sheets!")
    return redirect("home")

