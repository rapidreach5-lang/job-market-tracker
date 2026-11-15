import sqlite3
import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="Job Market Intelligence", page_icon="📊", layout="wide"
)

st.title("📊 Remote & Tech Job Market Intelligence Dashboard")
st.markdown(
    "Tracking market trends, job postings, and tech stack demand in real-time."
)


# Load data from SQLite
@st.cache_data
def load_data():
  conn = sqlite3.connect("jobs.db")
  df = pd.read_sql("SELECT * FROM jobs", conn)
  conn.close()
  return df


df = load_data()

# Display Metrics
col1, col2, col3 = st.columns(3)
col1.metric("Total Jobs Tracked", len(df))
col2.metric("Active Sources", df["source"].nunique() if not df.empty else 0)
col3.metric("Data Status", "Live / Local SQLite")

st.divider()

# Display Data Table
st.subheader("📋 Scraped Job Listings")
if not df.empty:
  st.dataframe(df, use_container_width=True)
else:
  st.info(
      "No data found in database yet. Run your scraper script to populate data!"
  )