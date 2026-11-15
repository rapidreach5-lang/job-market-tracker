from bs4 import BeautifulSoup
import requests


def scrape_jobs():
  # Example target URL (using a test scraping site or a target job board)
  url = "https://news.ycombinator.com/"  # Or a target tech board
  headers = {"User-Agent": "Mozilla/5.0"}

  response = requests.get(url, headers=headers)
  soup = BeautifulSoup(response.text, "html.parser")

  jobs = []
  # Extracting items (adjust tags based on the website you choose)
  items = soup.find_all("tr", class_="athing")

  for item in items:
    title_tag = item.find("span", class_="titleline")
    if title_tag:
      title = title_tag.text
      link = title_tag.find("a")["href"]
      jobs.append({"title": title, "source": link})

  return jobs


from database import init_db, save_jobs  # Import your database functions

if __name__ == "__main__":
  print("Scraping items...")
  scraped_data = scrape_jobs()

  # Initialize DB and save data automatically
  init_db()
  save_jobs(scraped_data)
  print(f"Successfully saved {len(scraped_data)} items to the database!")