import pandas as pd
from sqlalchemy import create_engine

def load_data():
    # Charger les données nettoyées
    df = pd.read_csv('data/clean_data.csv')
    
    # Connexion à la base de données PostgreSQL
    engine = create_engine('postgresql://user:password@localhost:5432/mydatabase')
    
    # Charger les données dans la table
    df.to_sql('clean_data', engine, if_exists='replace', index=False)
    print("Chargement réussi")

if __name__ == "__main__":
    load_data()
