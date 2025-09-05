# 🕵️ Django Job Scraper

A Django-based project that scrapes job postings (from **TimesJobs**) and saves them into a database.  
It can also update job listings to **Google Sheets** automatically.

---

## Create google api 
**Get api from google sheet  **

How to Get credentials.json for Google Sheets API

Go to Google Cloud Console

Open Google Cloud Console
.

Make sure you are signed in with your Google account.

Create a New Project

Click the project dropdown (top-left).

Select “New Project”, give it a name (e.g., Job Scraper), and click Create.

Enable Google Sheets API and Google Drive API

In the sidebar, go to APIs & Services > Library.

Search for Google Sheets API → Click Enable.

Do the same for Google Drive API (needed for access).

Create Service Account Credentials

Go to APIs & Services > Credentials.

Click + CREATE CREDENTIALS → Choose Service Account.

Enter a name (e.g., job-scraper-service), then click Done.

Generate a JSON Key File

In the Service Accounts list, click your new account.

Go to the Keys tab → Click Add Key → Create New Key.

Choose JSON → A file will be downloaded (this is your credentials.json).

Share Your Google Sheet with the Service Account

Open your Google Sheet (create one if you haven’t).

Copy the email address of your service account (something like job-scraper@your-project.iam.gserviceaccount.com).

Click Share in Google Sheets and paste the email → Give it Editor access.

Save the File in Your Project

Place the downloaded credentials.json file in your Django project folder.

Reference it in your code like this:


## 🚀 Features
- Scrape jobs from [TimesJobs](https://www.timesjobs.com).
- Extracts:
  - Title
  - Company
  - Location
  - Experience
  - Salary
  - Posted date
  - Description
  - Skills
  - Job link
- Stores jobs in **Django models** (avoids duplicates using unique link).
- Can push jobs into **Google Sheets** (optional).
- Simple web UI with button to trigger scraper.

---

## 🛠️ Tech Stack
- **Python 3.10+**
- **Django 5.x**
- **BeautifulSoup4**
- **Requests**
- **gspread** (Google Sheets API)
- **Selenium (optional, for sites with JS)**

---

## 📦 Installation

```bash
# 1. Clone repo
git clone https://github.com/coderdigi01/jobscraper.git
cd jobscraper

# 2. Create virtual environment
python -m venv env
source env/bin/activate   # Linux/Mac
env\Scripts\activate      # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Apply migrations
python manage.py migrate

# 5. Create superuser (optional)
python manage.py createsuperuser

# 6. Run server
python manage.py runserver
