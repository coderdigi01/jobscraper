import gspread
from oauth2client.service_account import ServiceAccountCredentials
from django.conf import settings

def get_google_sheet():
    scope = ["https://spreadsheets.google.com/feeds",
             "https://www.googleapis.com/auth/drive"]

    creds = ServiceAccountCredentials.from_json_keyfile_name(
        settings.GOOGLE_SHEET_CREDENTIALS, scope
    )
    client = gspread.authorize(creds)
    sheet = client.open(settings.GOOGLE_SHEET_NAME).sheet1
    return sheet

def update_sheet(job_data):
    sheet = get_google_sheet()
    existing = sheet.get_all_values()
    existing_links = {row[3] for row in existing[1:]} if len(existing) > 1 else set()

    # Add header if sheet is empty
    if not existing:
        sheet.append_row(["Title", "Company", "Location", "Link"])

    for job in job_data:
        if job["link"] not in existing_links:  # avoid duplicates
            sheet.append_row([job["title"], job["company"], job["location"], job["link"]])
