import pandas as pd
import numpy as np
import os

# Set seed for reproducibility
np.random.seed(42)

# Number of samples
num_samples = 500
num_features = 100  # Simulated static features (can adjust to 1000+ if needed)

# Simulate benign and malicious data (50-50)
benign_features = np.random.rand(num_samples // 2, num_features)
malicious_features = np.random.rand(num_samples // 2, num_features) + np.random.normal(0.1, 0.1, (num_samples // 2, num_features))  # Shifted distribution

# Combine and create labels
features = np.vstack([benign_features, malicious_features])
labels = np.array([0] * (num_samples // 2) + [1] * (num_samples // 2))  # 0 = benign, 1 = ransomware

# Create DataFrame
columns = [f"feature_{i}" for i in range(num_features)]
df = pd.DataFrame(features, columns=columns)
df["label"] = labels

# Save to CSV
os.makedirs("data", exist_ok=True)
df.to_csv("data/ransomware_data.csv", index=False)
print("✅ Synthetic ransomware dataset generated and saved to data/ransomware_data.csv")
