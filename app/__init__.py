from flask import Flask
from transformers import pipeline

app = Flask(__name__)

# Load pre-trained sentiment analysis model
sentiment_pipeline = pipeline("sentiment-analysis")

from app import routes