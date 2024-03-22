'''
Prediction function
'''
import numpy as np
import pandas as pd

# Version 1
# most_similar = 0 --> consider all users
# most_similar = 1 --> consider only the most similar users

def predict_rating(user_id, item_id, user_item_matrix, user_similarity, most_similar):
    # Calculate the mean rating of user a
    mean_rating_a = user_item_matrix.loc[user_id].mean()

    # Initialize the numerator and denominator of the formula
    numerator = 0
    denominator = 0
    dict_intern = user_similarity[user_id]

    if most_similar == 1:
        # Sort values
        dict_intern = {k: v for k, v in sorted(dict_intern.items(), key=lambda item: item[1], reverse=True)}
        users = list(dict_intern.keys())
        users = users[:50]
    else:
        users = dict_intern.keys()
    
    # Iterate over all users
    for other_user_id in users:
        # Check if user b has actually rated the item
        if not pd.isnull(user_item_matrix.loc[other_user_id, item_id]):
            # Calculate the mean rating of user b
            mean_rating_b = user_item_matrix.loc[other_user_id].mean()
            # Calculate the rating of b for item p
            rating_b_p = user_item_matrix.loc[other_user_id, item_id]
            # Update the numerator and denominator
            similarity = dict_intern[other_user_id]
            numerator += similarity * (rating_b_p - mean_rating_b)
            denominator += similarity
    
    # Calculate the predicted rating
    if denominator != 0:
        predicted_rating = mean_rating_a + (numerator / denominator)
    else:
        predicted_rating = mean_rating_a  # Avoid division by zero

    return predicted_rating

# Version 2 (abs at the denominator):
# most_similar = 0 --> consider all users
# most_similar = 1 --> consider only the most similar users

def predict_rating_with_abs(user_id, item_id, user_item_matrix, user_similarity, most_similar):
    # Calculate the mean rating of user a
    mean_rating_a = user_item_matrix.loc[user_id].mean()

    # Initialize the numerator and denominator of the formula
    numerator = 0
    denominator = 0
    dict_intern = user_similarity[user_id]

    if most_similar == 1:
        # Sort for value
        dict_intern = {k: v for k, v in sorted(dict_intern.items(), key=lambda item: item[1], reverse=True)}
        users = list(dict_intern.keys())
        users = users[:100]
    else:
        users = dict_intern.keys()
    
    # Iterate over all users
    for other_user_id in users:
        # Check if user b has actually rated the item
        if not pd.isnull(user_item_matrix.loc[other_user_id, item_id]):
            # Calculate the mean rating of user b
            mean_rating_b = user_item_matrix.loc[other_user_id].mean()
            # Calculate the rating of b for item p
            rating_b_p = user_item_matrix.loc[other_user_id, item_id]
            # Update the numerator and denominator
            similarity = dict_intern[other_user_id]
            numerator += similarity * (rating_b_p - mean_rating_b)
            denominator += abs(similarity)
            
    # Calculate the predicted rating
    if denominator != 0:
        predicted_rating = mean_rating_a + (numerator / denominator)
    else:
        predicted_rating = mean_rating_a  # Avoid division by zero

    return predicted_rating
