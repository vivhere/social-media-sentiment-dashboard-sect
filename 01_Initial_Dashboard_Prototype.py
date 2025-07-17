# 01_Initial_Dashboard_Prototype

## Project: Social Media Sentiment Dashboard (Prototype)
**Author:** Vivek Yadav  
**Phase:** UI and Sentiment Visualization (Static)

## Overview
This prototype is the first step in building a full-scale social media sentiment analysis dashboard. It demonstrates how sentiment data can be visually represented using Streamlit and Matplotlib with dummy data.

The current version is static and does **not** include live tweet scraping or NLP sentiment analysis yet. These will be added in future phases.

## Features Implemented
- Streamlit-based interactive UI
- Table display of sample sentiment-tagged posts
- Bar chart summarizing sentiment distribution
- Basic layout with headers, markdown, and visual plots

## Tech Stack
- Python
- Streamlit
- Pandas
- Matplotlib

## File
- `01_Initial_Dashboard_Prototype.py`  
  Streamlit app containing static layout and dummy sentiment visualization.

## How to Run

1. Install required libraries:
```bash
pip install streamlit pandas matplotlib
```

2. Launch the dashboard:
```bash
streamlit run 01_Initial_Dashboard_Prototype.py
```

3. Open the app in your browser (usually at `http://localhost:8501`).

## Sample Output

- Displays sample social media posts (Twitter and Reddit) with predefined sentiments.
- Shows a bar chart visualizing the count of each sentiment type (Positive, Negative, Neutral).

## Roadmap (Next Steps)
- Integrate real-time tweet scraping using `snscrape`
- Implement sentiment analysis using `TextBlob` or `VADER`
- Add filtering by platform, keyword, and sentiment
- Enhance visualizations using `plotly` or other libraries

---

> This version is primarily for UI and visualization validation before integrating dynamic components.
