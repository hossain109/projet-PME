#!/usr/bin/env python3
import sqlite3
import requests
import pandas as pd

# URLs des fichiers de données
url_ventes = "https://docs.google.com/spreadsheets/d/e/2PACX-1vSawI56WBC64foMT9pKCiY594fBZk9Lyj8_bxfgmq-8ck_jw1Z49qDeMatCWqBxehEVoM6U1zdYx73V/pub?gid=760830694&single=true&output=csv"
url_produits = "https://docs.google.com/spreadsheets/d/e/2PACX-1vSawI56WBC64foMT9pKCiY594fBZk9Lyj8_bxfgmq-8ck_jw1Z49qDeMatCWqBxehEVoM6U1zdYx73V/pub?gid=714623615&single=true&output=csv"
url_magasins = "https://docs.google.com/spreadsheets/d/e/2PACX-1vSawI56WBC64foMT9pKCiY594fBZk9Lyj8_bxfgmq-8ck_jw1Z49qDeMatCWqBxehEVoM6U1zdYx73V/pub?gid=714623615&single=true&output=csv
"

# Télécharger les données
def download_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.content
    else:
        raise Exception(f"Erreur lors du téléchargement des données depuis {url}")

# Importer les données dans la base de données
def import_data():
    conn = sqlite3.connect('/data/test.db')
    cursor = conn.cursor()

    # Importer les produits
    produits_data = download_data(url_produits)
    produits_df = pd.read_csv(pd.compat.StringIO(produits_data.decode('utf-8')))
    produits_df.to_sql('produits', conn, if_exists='append', index=False)

    # Importer les magasins
    magasins_data = download_data(url_magasins)
    magasins_df = pd.read_csv(pd.compat.StringIO(magasins_data.decode('utf-8')))
    magasins_df.to_sql('magasins', conn, if_exists='append', index=False)

    # Importer les ventes (uniquement les nouvelles données)
    ventes_data = download_data(url_ventes)
    ventes_df = pd.read_csv(pd.compat.StringIO(ventes_data.decode('utf-8')))
    ventes_df.to_sql('ventes', conn, if_exists='append', index=False)

    # Valider les changements
    conn.commit()
    conn.close()

    print("Données importées avec succès.")

# Exécuter l'importation
import_data()
