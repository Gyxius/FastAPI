import numpy as np
import json
from tensorflow.keras.preprocessing.text import tokenizer_from_json
from tensorflow.keras.models import load_model
from tensorflow.keras.utils import pad_sequences  # you can remove if already imported elsewhere

# Load tokenizer from JSON
with open("tokenizer.json", "r", encoding="utf-8") as f:
    tokenizer = tokenizer_from_json(f.read())

# Load model
model = load_model("my_model.keras")