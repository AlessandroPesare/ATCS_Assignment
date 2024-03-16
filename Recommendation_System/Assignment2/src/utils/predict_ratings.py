'''
Prediction function
'''
import numpy as np
import pandas as pd
# Version 1
# most_similar = 0 --> consider all users
# most_similar = 1 --> consider only the most similar users

def predict_rating(user_id, item_id, user_item_matrix,user_similarity,most_similar):
    # Calcola la media dei rating dell'utente a
    mean_rating_a = user_item_matrix.loc[user_id].mean()

    # Inizializza il numeratore e il denominatore della formula
    numerator = 0
    denominator = 0
    dict_intern = user_similarity[user_id]

    if(most_similar == 1):
        #sort values
        dict_intern = {k: v for k, v in sorted(dict_intern.items(), key=lambda item: item[1], reverse=True)}
        users = list(dict_intern.keys())
        users = users[:50]
    else:
        users = dict_intern.keys()
    # Itera su tutti gli utenti
    for other_user_id in users:
        # Verifica se l'utente b ha effettivamente valutato l'item
        if not pd.isnull(user_item_matrix.loc[other_user_id, item_id]):
            # Calcola la media dei rating dell'utente b
            mean_rating_b = user_item_matrix.loc[other_user_id].mean()
            # Calcola il rating di b per l'item p
            rating_b_p = user_item_matrix.loc[other_user_id, item_id]
            # Aggiorna il numeratore e il denominatore
            similarity = dict_intern[other_user_id]
            numerator += similarity * (rating_b_p - mean_rating_b)
            denominator += similarity
    # Calcola il rating predetto
    if denominator != 0:
        predicted_rating = mean_rating_a + (numerator / denominator)
    else:
        predicted_rating = mean_rating_a  # Evita la divisione per zero


    return predicted_rating

# Version 2 (abs at the denominator):
# most_similar = 0 --> consider all users
# most_similar = 1 --> consider only the most similar users

def predict_rating_with_abs(user_id, item_id, user_item_matrix,user_similarity,most_similar):
    # Calcola la media dei rating dell'utente a
    mean_rating_a = user_item_matrix.loc[user_id].mean()

    # Inizializza il numeratore e il denominatore della formula
    numerator = 0
    denominator = 0
    dict_intern = user_similarity[user_id]

    if(most_similar == 1):
        #sort for value
        dict_intern = {k: v for k, v in sorted(dict_intern.items(), key=lambda item: item[1], reverse=True)}
        users = list(dict_intern.keys())
        users = users[:50]
    else:
        users = dict_intern.keys()
    # Itera su tutti gli utenti
    for other_user_id in users:
        # Verifica se l'utente b ha effettivamente valutato l'item
        if not pd.isnull(user_item_matrix.loc[other_user_id, item_id]):
            # Calcola la media dei rating dell'utente b
            mean_rating_b = user_item_matrix.loc[other_user_id].mean()
            # Calcola il rating di b per l'item p
            rating_b_p = user_item_matrix.loc[other_user_id, item_id]
            # Aggiorna il numeratore e il denominatore
            similarity = dict_intern[other_user_id]
            numerator += similarity * (rating_b_p - mean_rating_b)
            denominator += abs(similarity)
            
    # Calcola il rating predetto
    if denominator != 0:
        predicted_rating = mean_rating_a + (numerator / denominator)
    else:
        predicted_rating = mean_rating_a  # Evita la divisione per zero


    return predicted_rating
