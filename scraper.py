from database import init_db, save_jobs
import requests


def scrape_jobs():
  url = "https://remoteok.com/api"
  headers = {"User-Agent": "Mozilla/5.0"}

  response = requests.get(url, headers=headers)
  data = response.json()

  jobs = []
  for item in data[1:]:
    title = item.get("position")
    company = item.get("company")
    url_link = item.get("url")
    # Grab the minimum salary, default to 0 if the employer didn't list one
    salary = item.get("salary_min", 0) or 0

    if title and company:
      jobs.append({
          "title": f"{title} at {company}",
          "source": url_link,
          "salary_min": int(salary),
      })

  return jobs


if __name__ == "__main__":
  print("Fetching remote jobs and salaries...")
  scraped_data = scrape_jobs()

  init_db()
  save_jobs(scraped_data)
  print(f"Successfully saved {len(scraped_data)} jobs with salary data!")