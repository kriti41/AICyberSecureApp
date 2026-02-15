import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import classification_report
import joblib
import os

# Create models folder if not exists
os.makedirs("models", exist_ok=True)

# Load dataset
train_df = pd.read_csv("ids_data/KDDTrain+.csv", header=None)
test_df = pd.read_csv("ids_data/KDDTest+.csv", header=None)

# Add column names (based on NSL-KDD feature list)
column_names = [f"f{i}" for i in range(41)] + ["label", "difficulty"]
train_df.columns = column_names
test_df.columns = column_names

# Drop 'difficulty' column
train_df.drop(columns=["difficulty"], inplace=True)
test_df.drop(columns=["difficulty"], inplace=True)

# Encode categorical features
categorical_cols = ["f1", "f2", "f3"]
encoder = LabelEncoder()
for col in categorical_cols:
    train_df[col] = encoder.fit_transform(train_df[col])
    test_df[col] = encoder.transform(test_df[col])

# Convert labels: 'normal' = 0, everything else = 1 (attack)
train_df["label"] = train_df["label"].apply(lambda x: 0 if x == "normal" else 1)
test_df["label"] = test_df["label"].apply(lambda x: 0 if x == "normal" else 1)

# Separate features and labels
X_train = train_df.drop(columns=["label"])
y_train = train_df["label"]
X_test = test_df.drop(columns=["label"])
y_test = test_df["label"]

# Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred))

# Save model
joblib.dump(model, "models/ids_model.pkl")
print("✅ IDS model saved to models/ids_model.pkl")
