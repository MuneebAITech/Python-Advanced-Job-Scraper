import requests
from bs4 import BeautifulSoup


def scrape_jobs(url):

    response = requests.get(url)

    if response.status_code != 200:
        raise Exception(
            f"Failed to connect. Status Code: {response.status_code}"
        )

    soup = BeautifulSoup(
        response.text,
        "html.parser"
    )

    jobs = []

    job_cards = soup.find_all(
        "div",
        class_="card-content"
    )

    for card in job_cards:
    

        title = card.find(
            "h2",
            class_="title"
        ).text.strip()

        company = card.find(
            "h3",
            class_="company"
        ).text.strip()

        location = card.find(
            "p",
            class_="location"
        ).text.strip()

        date_posted = card.find(
            "time"
        )["datetime"]

        apply_link = card.find_all(
            "a",
            class_="card-footer-item"
        )[1]["href"]

        jobs.append(
            {
                "title": title,
                "company": company,
                "location": location,
                "date_posted": date_posted,
                "apply_link": apply_link
            }
        )
    return jobs