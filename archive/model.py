# from transformers import pipeline

# # classifier = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")
# classifier = pipeline("sentiment-analysis", model="Seethal/sentiment_analysis_generic_dataset")


# def predict_sentiment(sample_text = "The movie was terrible, i will not recommend this movie to anyone"):
#     # Don't forget to tokenize & pad!
#     texts = [sample_text]
#     results = classifier(texts)

#     for text, result in zip(texts, results):
#         return result['label']