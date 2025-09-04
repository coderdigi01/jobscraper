# 🕵️ Django Job Scraper

A Django-based project that scrapes job postings (from **TimesJobs**) and saves them into a database.  
It can also update job listings to **Google Sheets** automatically.

---

## Create google api 
**Get api from google sheet  **

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
