# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 12:31:13 2025

@author: HP
"""

# Import necessary libraries
import pandas as pd
import numpy as np
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

# Download NLTK resources
nltk.download('stopwords')
nltk.download('punkt')

# Load the dataset
news = pd.read_csv("WELFake_Dataset.csv", encoding='latin1')  # Try 'latin1' or 'ISO-8859-1'


news = pd.read_csv("C:/Users/HP/Downloads/WELFake_Dataset.csv")  # Replace with your dataset file
print("Dataset loaded successfully.")
try:
    news = pd.read_csv("C:/Users/HP/Downloads/WELFake_Dataset.csv")  # Replace with your dataset file
    print("Dataset loaded successfully.")
except FileNotFoundError:
    print("Error: Dataset file not found. Check the file path.")
    raise

# Inspect the dataset
print(news.head())
print(news.info())
print(news.isna().sum())

# Fill missing values
news.fillna(' ', inplace=True)

# Combine 'title' and 'text' for better context
news['content'] = news['title'] + " " + news['text']

# Drop unnecessary columns
news = news[['content', 'label']]  # Keep only content and label columns

# Initialize the stemmer
ps = PorterStemmer()

# Define text preprocessing function
def preprocess_text(text):
    # Remove non-alphabetic characters
    text = re.sub('[^a-zA-Z]', ' ', text)
    # Convert to lowercase
    text = text.lower()
    # Tokenize and remove stopwords
    words = [ps.stem(word) for word in word_tokenize(text) if word not in stopwords.words('english')]
    return " ".join(words)

# Apply preprocessing
news['content'] = news['content'].apply(preprocess_text)

# Split the dataset into training and testing sets
X = news['content']
y = news['label']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Feature extraction using TF-IDF Vectorizer
tfidf = TfidfVectorizer(max_features=5000)
X_train_tfidf = tfidf.fit_transform(X_train).toarray()
X_test_tfidf = tfidf.transform(X_test).toarray()

# Build and train the Logistic Regression model
model = LogisticRegression()
model.fit(X_train_tfidf, y_train)

# Make predictions
y_pred = model.predict(X_test_tfidf)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.2f}")

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# Confusion Matrix
cm = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(6, 4))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=['Fake', 'Real'], yticklabels=['Fake', 'Real'])
plt.xlabel("Predicted")
plt.ylabel("True")
plt.title("Confusion Matrix")
plt.show()

# Save the model and vectorizer (optional)
import pickle
with open('fake_news_model.pkl', 'wb') as model_file:
    pickle.dump(model, model_file)
with open('tfidf_vectorizer.pkl', 'wb') as vectorizer_file:
    pickle.dump(tfidf, vectorizer_file)

print("Model and vectorizer saved successfully.")
