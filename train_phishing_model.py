import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib

# Load dataset
df = pd.read_csv("data/phishing_data.csv")
X = df[['url_length', 'has_https', 'domain_length', 'dot_count']]
y = df['label']

# Train model
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Save model
joblib.dump(model, "models/phishing_model.pkl")
print("✅ Model saved to models/phishing_model.pkl")
