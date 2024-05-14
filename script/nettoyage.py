import matplotlib.pyplot as plt
import spacy

from datasets import load_dataset

dataset = load_dataset("rajpurkar/squad", split='train')
dataset = dataset.to_pandas()

nlp = spacy.load("en_core_web_sm")

dataset["context_length"]=None
for i, element in enumerate(dataset.itertuples()):
    doc = nlp(element.context)
    dataset.loc[i, "context_length"] = len(doc)
    if i>200:
        break

dataset["context_length"].plot(kind="hist")

# Définition du chemin du fichier de sortie
path = '../data/output_textes.txt'

# Écriture de la sortie dans un fichier
with open(path, 'w') as f:
    f.write(df.head(nombre_articles).to_string())