import pandas as pd

def transform_data():
    # Charger les données brutes
    df = pd.read_json('data/raw_data.json')
    
    # Transformation : garder uniquement certaines colonnes
    df_clean = df[['id', 'title', 'body']].dropna()
    
    # Sauvegarder les données nettoyées
    df_clean.to_csv('data/clean_data.csv', index=False)
    print("Transformation réussie")

if __name__ == "__main__":
    transform_data()
