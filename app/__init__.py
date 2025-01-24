from flask import Flask
from transformers import pipeline

app = Flask(__name__)

# Load pre-trained sentiment analysis model
sentiment_pipeline = pipeline("sentiment-analysis", model="nlptown/bert-base-multilingual-uncased-sentiment")

from app import routes