'''POINT A'''

import pandas as pd
import os

# Ottieni il percorso della cartella del progetto
project_folder = os.path.dirname(os.path.dirname(__file__))  # Risale di due directory dal percorso dello script

# Costruisci i percorsi completi dei file CSV
links_file_path = os.path.join(project_folder, 'dataset', 'links.csv')
movies_file_path = os.path.join(project_folder, 'dataset', 'movies.csv')
ratings_file_path = os.path.join(project_folder, 'dataset', 'ratings.csv')
tags_file_path = os.path.join(project_folder, 'dataset', 'tags.csv')

# Leggi i file CSV
links_df = pd.read_csv(links_file_path)
movies_df = pd.read_csv(movies_file_path)
ratings_df = pd.read_csv(ratings_file_path)
tags_df = pd.read_csv(tags_file_path)

# Visualizza le prime righe di ciascun DataFrame
print("Primi 5 elementi di links.csv:")
print(links_df.head())

print("\nPrimi 5 elementi di movies.csv:")
print(movies_df.head())

print("\nPrimi 5 elementi di rating.csv:")
print(ratings_df.head())

print("\nPrimi 5 elementi di tags.csv:")
print(tags_df.head())

# Conta il numero di elementi in ciascun DataFrame
print("\nNumero di elementi in links.csv:", len(links_df))
print("Numero di elementi in movies.csv:", len(movies_df))
print("Numero di elementi in rating.csv:", len(ratings_df))
print("Numero di elementi in tags.csv:", len(tags_df))
