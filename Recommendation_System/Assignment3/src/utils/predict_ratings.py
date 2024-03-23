'''
Prediction function
'''
import numpy as np
import pandas as pd



def user_ratings(group_users,user_item_matrix):
    """
    Creates a dictionary mapping each user in the group to a list of movies they have rated, along with their corresponding ratings.

    Parameters:
    group_users (list): List of user IDs in the group.
    user_item_matrix (DataFrame): DataFrame where user_item_matrix.loc[i][j] represents the rating of user i on item j.

    Returns:
    dict: A dictionary where keys are user IDs and values are lists of tuples (movie_id, rating),
          representing the movies rated by each user in the group and their corresponding ratings.
    """
    movies2ratings = {}
    # Iterate over each user in the group
    for user_id in group_users:
        # Initialize an empty list to store the rated movies and their ratings for the current user
        movies2ratings[user_id] = []
        # Iterate over each movie in the user_item_matrix columns
        for movie_id in user_item_matrix.columns:
            # Get the rating of the current user for the current movie
            rating = user_item_matrix.loc[user_id][movie_id]
            # If the rating is not NaN (i.e., the user has rated the movie), add it to the list
            if not np.isnan(rating):
                movies2ratings[user_id].append((movie_id,rating))
    return movies2ratings


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
