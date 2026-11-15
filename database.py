import sqlite3


def init_db():
  conn = sqlite3.connect("jobs.db")
  cursor = conn.cursor()
  cursor.execute("""
        CREATE TABLE IF NOT EXISTS jobs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            source TEXT,
            date_added TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
  conn.commit()
  conn.close()


def save_jobs(jobs):
  conn = sqlite3.connect("jobs.db")
  cursor = conn.cursor()
  for job in jobs:
    cursor.execute(
        "INSERT INTO jobs (title, source) VALUES (?, ?)",
        (job["title"], job["source"]),
    )
  conn.commit()
  conn.close()


if __name__ == "__main__":
  init_db()
  print("Database initialized successfully!")