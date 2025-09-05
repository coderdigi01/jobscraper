import requests
from bs4 import BeautifulSoup
from .models import Job  # make sure this import is correct


def parse_job_card(card):
    # Title
    title_tag = card.find("h2", class_="heading-trun")
    title = title_tag.get_text(strip=True) if title_tag else "N/A"

    # Company
    company_tag = card.find("h3", class_="joblist-comp-name")
    company = company_tag.get_text(strip=True) if company_tag else "N/A"

    # Posted date
    posted_tag = card.find("span", class_="sim-posted")
    posted = posted_tag.get_text(strip=True) if posted_tag else "N/A"

    # Job description snippet
    desc_tag = card.find("li", class_="job-description__")
    description = desc_tag.get_text(strip=True) if desc_tag else "N/A"

    # Skills
    skills_div = card.find("div", class_="more-skills-sections")
    skills = [s.get_text(strip=True) for s in skills_div.find_all("span") if "more" not in s.get_text().lower()] if skills_div else []

    # Location, Experience, Salary
    details = card.find("ul", class_="top-jd-dtl")
    location, experience, salary = "N/A", "N/A", "N/A"
    if details:
        detail_items = details.find_all("li")
        if len(detail_items) > 0:
            location = detail_items[0].get_text(strip=True)
        if len(detail_items) > 1:
            experience = detail_items[1].get_text(strip=True)
        if len(detail_items) > 2:
            salary = detail_items[2].get_text(strip=True)

    # Job link
    link_tag = card.find("a", class_="posoverlay_srp")
    link = link_tag["href"] if link_tag else "N/A"

    return {
        "title": title,
        "company": company,
        "posted": posted,
        "description": description,
        "skills": skills,
        "location": location,
        "experience": experience,
        "salary": salary,
        "link": link,
    }



def scrape_jobs():
    url = "https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Python+developer&txtLocation=India"
    response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    soup = BeautifulSoup(response.text, "html.parser")

    container = soup.find("ul", class_="new-joblist")
    if not container:
        print("No job list found!")
        return []

    cards = container.find_all("li", class_="clearfix job-bx wht-shd-bx")
    print(f"Found {len(cards)} jobs")

    jobs = []
    for card in cards:
        job_data = parse_job_card(card)

        # Save if not exists
        if not Job.objects.filter(link=job_data["link"]).exists():
            Job.objects.create(
                title=job_data["title"],
                company=job_data["company"],
                location=job_data["location"],
                experience=job_data["experience"],
                salary=job_data["salary"],
                posted=job_data["posted"],
                description=job_data["description"],
                skills=", ".join(job_data["skills"]),  # convert list to string
                link=job_data["link"],
            )

        jobs.append(job_data)

    return jobs




