# Social Media Sentiment Dashboard

A data-driven sentiment analysis dashboard built using Python and Streamlit, designed to collect and visualize public opinion from platforms like Twitter (X) and Reddit.

---
# Initial Dashboard Prototype

## Overview
This prototype is the first step in building a comprehensive Twitter Sentiment Dashboard using Streamlit. It focuses on setting up the foundational layout and UI of the dashboard before integrating data scraping or sentiment analysis functionalities.

## File Included
- `01_Initial_Dashboard_Prototype.py`  
  → A basic Streamlit app with a sidebar, placeholder tabs for future visualizations, and layout structure.

## How to Run
Make sure Streamlit is installed:

```bash
pip install streamlit
```

Then run the app:

```bash
streamlit run 01_Initial_Dashboard_Prototype.py
```

This will open a local dashboard in your browser.

## Current Progress
- Streamlit interface is successfully launched.
- UI sections for visual analytics (Top Hashtags, Tweet Count, Polarity) are created as placeholders.
- Sidebar navigation is ready.
- Responsive layout is tested.

## Features

- Scrapes tweets based on keyword and date range
- Analyzes sentiment (positive, neutral, negative)
- Interactive Streamlit dashboard to view trends
- Data saved in CSV format for transparency and reproducibility
- Modular code structure (dashboard, scraping, and analysis separated)

---

## Tech Stack

- Python 3.13
- Streamlit
- snscrape
- pandas
- TextBlob (planned: VADER)
- matplotlib / seaborn (optional for custom visuals)

---

## Folder Structure
📄 [Click here to view the Dashboard Preview (PDF)](Social%20Media%20Sentiment%20Dashboard.pdf)

