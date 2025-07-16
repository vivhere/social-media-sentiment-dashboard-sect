# Social Media Sentiment Dashboard

A data-driven sentiment analysis dashboard built using Python and Streamlit, designed to collect and visualize public opinion from platforms like Twitter (X) and Reddit.

---

## Project Overview

This application collects public posts using `snscrape` from Twitter (X), analyzes their sentiment using NLP techniques such as TextBlob or VADER, and displays the results in an interactive web dashboard using Streamlit. The goal is to help users understand public perception around a given keyword, event, or brand.

---

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

