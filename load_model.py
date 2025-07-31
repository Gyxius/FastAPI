import numpy as np
import pickle
from keras.utils import pad_sequences
from tensorflow.keras.models import load_model

def dummy_npwarn_decorator_factory():
  def npwarn_decorator(x):
    return x
  return npwarn_decorator
np._no_nep50_warning = getattr(np, '_no_nep50_warning', dummy_npwarn_decorator_factory)



with open("tokenizer.pkl", "rb") as f:
    tokenizer = pickle.load(f)

model = load_model("my_model.keras")

