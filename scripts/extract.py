import requests
import json

def extract_data():
    url = 'https://jsonplaceholder.typicode.com/posts'  # API d'exemple
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        with open('data/raw_data.json', 'w') as f:
            json.dump(data, f)
        print("Extraction réussie")
    else:
        print(f"Erreur lors de l'extraction : {response.status_code}")

if __name__ == "__main__":
    extract_data()
