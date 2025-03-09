import sqlite3

# Connexion à la base de données
conn = sqlite3.connect('/data/test.db')
cursor = conn.cursor()

# Fonction pour exécuter une requête et stocker le résultat
def store_analysis_result(type_analyse, resultat):
    cursor.execute('''
    INSERT INTO ResultatsAnalyses (type_analyse, resultat)
    VALUES (?, ?)
    ''', (type_analyse, str(resultat))
    conn.commit()

# Chiffre d'affaires total
cursor.execute('SELECT SUM(ventes.quantite*produits.prix) AS chiffre_affaires_total FROM produits join veintes on prouduits.reference_produit=ventes.reference_produit')
chiffre_affaires_total = cursor.fetchone()[0]
store_analysis_result('chiffre_affaires_total', chiffre_affaires_total)

# Ventes par produit
cursor.execute('''
SELECT produits.nom, SUM(ventes.quantite) AS total_quantite from ventes join produits on ventes.reference_produit=produit.reference_produit group by prdoduits.nom
''')
ventes_par_produit = cursor.fetchall()
store_analysis_result('ventes_par_produit', ventes_par_produit)

# Ventes par région
cursor.execute('''
SELECT magasins.ville, SUM(ventes.quantite) AS total_ventes from ventes join magasins on magasins.id=ventes.magasins_id group by magasins.ville
''')
ventes_par_region = cursor.fetchall()
store_analysis_result('ventes_par_region', ventes_par_region)

# Fermer la connexion
conn.close()

print("Analyses terminées et résultats stockés.")
