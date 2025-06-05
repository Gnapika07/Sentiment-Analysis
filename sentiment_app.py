import streamlit as st
from textblob import TextBlob
import matplotlib.pyplot as plt

st.title("📝 Sentiment Analysis App")
st.write("This app uses TextBlob to analyze the sentiment of your text.")

text_input = st.text_area("Enter your review or comment here:")

if text_input:
    blob = TextBlob(text_input)
    polarity = blob.sentiment.polarity

    if polarity > 0:
        sentiment = "😊 Positive"
    elif polarity < 0:
        sentiment = "😠 Negative"
    else:
        sentiment = "😐 Neutral"

    st.write(f"**Sentiment:** {sentiment}")
    st.write(f"**Polarity Score:** {polarity:.2f}")

    # Pie chart
    labels = ['Positive', 'Negative', 'Neutral']
    sizes = [max(polarity, 0), abs(min(polarity, 0)), 1 - abs(polarity)]
    colors = ['green', 'red', 'gray']
    plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%')
    plt.title('Sentiment Distribution')
    st.pyplot(plt)
