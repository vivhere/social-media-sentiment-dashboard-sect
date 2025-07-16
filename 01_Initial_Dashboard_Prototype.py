# Project: Social Media Sentiment Dashboard (Prototype)
# Author: Vivek Yadav
# Phase: UI and Sentiment Visualization

# --------------------------
# Step 1: Import Libraries
# --------------------------
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# --------------------------
# Step 2: Setup Streamlit Page
# --------------------------
st.set_page_config(page_title="Social Media Sentiment Dashboard", layout="wide")
st.title("Social Media Sentiment Dashboard (Prototype)")

st.markdown("""
This prototype demonstrates how sentiment data can be displayed and summarized using basic dummy data.
The live tweet scraping and NLP parts will be added in future phases.
""")

# --------------------------
# Step 3: Sample Dataset
# --------------------------
data = {
    "Platform": ["Twitter", "Reddit", "Twitter", "Reddit", "Twitter"],
    "Text": [
        "This product is amazing!",
        "Not satisfied with the quality.",
        "Absolutely loved it.",
        "Worst experience ever.",
        "It's okay, nothing special."
    ],
    "Sentiment": ["Positive", "Negative", "Positive", "Negative", "Neutral"]
}

df = pd.DataFrame(data)

# --------------------------
# Step 4: Show Data
# --------------------------
st.subheader("Sample Data")
st.dataframe(df)

# --------------------------
# Step 5: Sentiment Summary
# --------------------------
st.subheader("Sentiment Distribution")

sentiment_counts = df['Sentiment'].value_counts()
fig, ax = plt.subplots()
sentiment_counts.plot(kind='bar', color=['green', 'red', 'gray'], ax=ax)
plt.title("Count of Sentiment Types")
plt.xlabel("Sentiment")
plt.ylabel("Count")
st.pyplot(fig)

# --------------------------
# Step 6: Conclusion
# --------------------------
st.markdown("""
### Notes:
- This is a static dashboard based on sample data.
- Real-time scraping from Twitter will be integrated using `snscrape` in the next update.
- NLP sentiment analysis using `TextBlob` or `VADER` will also be integrated in the next version.
""")
