#!/bin/bash
# scripts/init_db.sh

# Créer la base de données et les tables
sqlite3 /data/test.db "
CREATE TABLE IF NOT EXISTS produits (
    id INTEGER PRIMARY KEY,
    nom TEXT,
    reference_produit TEXT UNIQUE,
    prix REAL,
    stock INTEGER
);
CREATE TABLE IF NOT EXISTS magasins (
    id INTEGER PRIMARY KEY,
    ville TEXT,
    nom_salary INTEGER
);


CREATE TABLE IF NOT EXISTS ventes (
    id INTEGER PRIMARY KEY,
    date_vente TEXT,
    reference_produit TEXT,
    magasin_id INTEGER,
    quantite INTEGER,
    FOREIGN KEY (reference_produit) REFERENCES Produits(reference_produit),
    FOREIGN KEY (magasin_id) REFERENCES Magasins(id)
);

CREATE TABLE IF NOT EXISTS vente_anaylysis(
   id INTEGER PRIMARY KEY,
   total  REAL
   produit TEXT
   region TEXT
);
"

echo "Base de données initialisée avec succès."
