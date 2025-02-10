import nltk

# Download required NLTK models (Run this only once)
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('vader_lexicon')

import streamlit as st
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist
from nltk.sentiment import SentimentIntensityAnalyzer

# Download necessary datasets (run only once)
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('vader_lexicon')

# Function for text summarization
def summarize_text(text, num_sentences=3):
    sentences = sent_tokenize(text)
    words = word_tokenize(text.lower())

    # Remove stopwords
    stop_words = set(stopwords.words("english"))
    filtered_words = [word for word in words if word.isalnum() and word not in stop_words]

    # Calculate word frequency
    freq_dist = FreqDist(filtered_words)

    # Score sentences based on word importance
    sentence_scores = {sent: sum(freq_dist[word] for word in word_tokenize(sent.lower()) if word in freq_dist)
                       for sent in sentences}

    # Select top sentences
    summary_sentences = sorted(sentence_scores, key=sentence_scores.get, reverse=True)[:num_sentences]
    
    return " ".join(summary_sentences)

# Function for sentiment analysis
def analyze_sentiment(text):
    sia = SentimentIntensityAnalyzer()
    score = sia.polarity_scores(text)
    
    if score["compound"] >= 0.05:
        return "😊 Positive"
    elif score["compound"] <= -0.05:
        return "😡 Negative"
    else:
        return "😐 Neutral"

# Streamlit UI
st.set_page_config(page_title="AI Text Processing Tool", page_icon="📜")
st.title("📜 AI-Powered Text Summarization & Sentiment Analysis")

# User input
text_input = st.text_area("Enter your text here:", height=200)

if st.button("Process Text"):
    if text_input:
        summary = summarize_text(text_input)
        sentiment = analyze_sentiment(text_input)

        st.subheader("📝 Summary")
        st.write(summary)

        st.subheader("📊 Sentiment Analysis")
        st.write(sentiment)
    else:
        st.warning("Please enter some text to analyze.")
