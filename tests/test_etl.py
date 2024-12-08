import os
from sqlalchemy import create_engine

def test_extraction():
    assert os.path.exists('data/raw_data.json'), "Extraction échouée : fichier manquant"

def test_transformation():
    assert os.path.exists('data/clean_data.csv'), "Transformation échouée : fichier manquant"

def test_load():
    engine = create_engine('postgresql://user:password@localhost:5432/mydatabase')
    result = engine.execute("SELECT COUNT(*) FROM clean_data")
    count = result.fetchone()[0]
    assert count > 0, "Chargement échoué : aucune donnée en base"
