import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import joblib  # To save the model

# Load sample data
df = pd.read_csv("sample_logs.csv")
logs = df['error_message'].tolist()
labels = df['error_type'].tolist()

# Train model
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(logs)
model = MultinomialNB().fit(X, labels)

# Save model & vectorizer for later use
joblib.dump(model, 'error_classifier_model.joblib')
joblib.dump(vectorizer, 'vectorizer.joblib')