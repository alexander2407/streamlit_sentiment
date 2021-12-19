import streamlit as st
import inference
from transformers import pipeline

st.title("Sentiment Analysis Web App - Deployed by GitHub Workflow")

# this uses distilbert-base-uncased-finetuned-sst-2-english
classifier = pipeline("sentiment-analysis", model = "distilbert-base-uncased-finetuned-sst-2-english")

user_input = st.text_input("Enter English Sentence to get sentiment: ", "I love sentiment analysis")

if st.button("Get sentiment"):
    output = inference.inference(classifier, user_input)
    label = (output[0]['label'])
    score = (output[0]['score'])

    st.write(f"Sentence: \"{user_input}\" has the sentiment {label} with a score of {score}")
