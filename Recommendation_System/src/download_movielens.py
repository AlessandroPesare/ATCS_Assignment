'''
POINT A:
 Download the MovieLens 100K rating dataset from https://grouplens.org/datasets/
movielens/ (the small dataset recommended for education and development). Read the
dataset, display the first few rows to understand it, and display the count of ratings (rows)
in the dataset to be sure that you download it correctly.
'''

import pandas as pd
import os


project_folder = os.path.dirname(os.path.dirname(__file__))  # Risale di due directory dal percorso dello script

links_file_path = os.path.join(project_folder, 'dataset', 'links.csv')
movies_file_path = os.path.join(project_folder, 'dataset', 'movies.csv')
ratings_file_path = os.path.join(project_folder, 'dataset', 'ratings.csv')
tags_file_path = os.path.join(project_folder, 'dataset', 'tags.csv')

# Read CSV
links_df = pd.read_csv(links_file_path)
movies_df = pd.read_csv(movies_file_path)
ratings_df = pd.read_csv(ratings_file_path)
tags_df = pd.read_csv(tags_file_path)

#
print("Primi 5 elementi di links.csv:")
print(links_df.head())

print("\nPrimi 5 elementi di movies.csv:")
print(movies_df.head())

print("\nPrimi 5 elementi di rating.csv:")
print(ratings_df.head())

print("\nPrimi 5 elementi di tags.csv:")
print(tags_df.head())

# Count element in each DataFrame
print("\nNumero di elementi in links.csv:", len(links_df))
print("Numero di elementi in movies.csv:", len(movies_df))
print("Numero di elementi in rating.csv:", len(ratings_df))
print("Numero di elementi in tags.csv:", len(tags_df))
