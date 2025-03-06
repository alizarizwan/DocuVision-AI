import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Sample dataset (Modify based on real data)
texts = ["technical drawing with schematics", "financial document", "mechanical engineering blueprint"]
labels = [0, 1, 2]  # 0 = Engineering, 1 = Finance, 2 = Mechanical

# Tokenization
tokenizer = Tokenizer(num_words=1000)
tokenizer.fit_on_texts(texts)
sequences = tokenizer.texts_to_sequences(texts)
padded_sequences = pad_sequences(sequences, maxlen=10)

# Define LSTM Model
model = Sequential([
    Embedding(input_dim=1000, output_dim=16, input_length=10),
    LSTM(32),
    Dense(3, activation="softmax")
])

model.compile(loss="sparse_categorical_crossentropy", optimizer="adam", metrics=["accuracy"])

# Train Model
model.fit(padded_sequences, labels, epochs=5)

def predict_text_class(text):
    """Predicts the category of extracted text."""
    seq = tokenizer.texts_to_sequences([text])
    padded = pad_sequences(seq, maxlen=10)
    prediction = model.predict(padded)
    return prediction.argmax()

# Example Usage:
if __name__ == "__main__":
    prediction = predict_text_class("This document contains engineering specifications.")
    print(f"Predicted Category: {prediction}")
