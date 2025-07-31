from load_model import *


def predict_sentiment(tokenizer, sample_text = "The movie was terrible, i will not recommend this movie to anyone"):
    # Don't forget to tokenize & pad!
    print(tokenizer)
    sequences = tokenizer.texts_to_sequences([sample_text])
    padded = pad_sequences(sequences, padding='post', maxlen=35)

    predictions = model.predict(padded)
    predicted_class_index = predictions.argmax(axis=-1)
    if predicted_class_index[0] == 0:
        return "Postive Sentiment"
    elif predicted_class_index[0] == 1:
        return "Negative Sentiment"
    else:
        return "Neutral Sentiment"