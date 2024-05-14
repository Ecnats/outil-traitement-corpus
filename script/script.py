import pyarrow.parquet as pq
import pandas as pd

# Lecture des données Parquet dans un DataFrame Pandas
table = pq.read_table('../data/test-00000-of-00001.parquet')
df = table.to_pandas()


# Nombre d'articles à afficher
nombre_articles = 50

# Affichage des premières lignes du DataFrame
print(df.head(nombre_articles))

# Définition du chemin du fichier de sortie
path = '../data/output_textes.txt'

# Écriture de la sortie dans un fichier
with open(path, 'w') as f:
    f.write(df.head(nombre_articles).to_string())