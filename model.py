# from load_model import *
# from transformers import pipeline

# classifier = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

# def predict_sentiment(sample_text = "The movie was terrible, i will not recommend this movie to anyone"):
#     # Don't forget to tokenize & pad!
#     texts = [sample_text]
#     results = classifier(texts)

#     for text, result in zip(texts, results):
#         return result['label']