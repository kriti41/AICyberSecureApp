import os
import requests

# Folder to save files
os.makedirs("ids_data", exist_ok=True)

urls = {
    "KDDTrain+.csv": "https://raw.githubusercontent.com/defcom17/NSL_KDD/master/KDDTrain+.csv",
    "KDDTest+.csv": "https://raw.githubusercontent.com/defcom17/NSL_KDD/master/KDDTest+.csv"
}

for name, url in urls.items():
    print(f"📥 Downloading {name}...")
    response = requests.get(url)
    with open(f"ids_data/{name}", "wb") as f:
        f.write(response.content)

print("✅ All files downloaded to 'ids_data/'")
