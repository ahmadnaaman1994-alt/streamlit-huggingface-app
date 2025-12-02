import streamlit as st
from transformers import pipeline

@st.cache_resource
def load_model():
    return pipeline(
        "sentiment-analysis",
        model="nlptown/bert-base-multilingual-uncased-sentiment"
    )

classifier = load_model()

st.title("Multilingual Sentiment Analysis App")
st.write("Enter a text below and get the sentiment prediction (1–5 stars).")

text = st.text_area("Input text here...")

if st.button("Analyze"):
    if text.strip():
        result = classifier(text)[0]
        st.success(f"Prediction: {result['label']}")
        st.info(f"Confidence: {result['score']:.4f}")
    else:
        st.warning("Please enter text before analyzing.")
