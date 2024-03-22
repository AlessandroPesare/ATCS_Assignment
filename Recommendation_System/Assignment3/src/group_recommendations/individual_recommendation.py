# RECOMMENDATION FUNCTION
import sys
import os

utils_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'utils'))
sys.path.append(utils_path)

import numpy as np
import pandas as pd
from predict_ratings import predict_rating, predict_rating_with_abs


def recommended_movies(user_id, user_item_matrix, user_similarity,most_similar):
    predicted_ratings = []

    unrated_movies = user_item_matrix.columns[user_item_matrix.loc[user_id].isnull()]

    for item_id in unrated_movies:
        predicted_rating = predict_rating(user_id, item_id, user_item_matrix, user_similarity,most_similar)
        predicted_ratings.append((item_id, predicted_rating))

    recommendations = sorted(predicted_ratings, key=lambda x: x[1], reverse=True)

    return recommendations

def recommended_movies_abs(user_id, user_item_matrix, user_similarity,most_similar):
    predicted_ratings = []

    unrated_movies = user_item_matrix.columns[user_item_matrix.loc[user_id].isnull()]

    for item_id in unrated_movies:
        predicted_rating = predict_rating_with_abs(user_id, item_id, user_item_matrix, user_similarity,most_similar)
        predicted_ratings.append((item_id, predicted_rating))

    recommendations = sorted(predicted_ratings, key=lambda x: x[1], reverse=True)

    return recommendations
    
# Version 1

def top_recommended_movies(user_id, user_item_matrix, user_similarity, num_recommendations, most_similar):

    predicted_ratings = []

    unrated_movies = user_item_matrix.columns[user_item_matrix.loc[user_id].isnull()]

    for item_id in unrated_movies:
        predicted_rating = predict_rating(user_id, item_id, user_item_matrix, user_similarity,most_similar)
        predicted_ratings.append((item_id, predicted_rating))

    top_recommendations = sorted(predicted_ratings, key=lambda x: x[1], reverse=True)[:num_recommendations]

    return top_recommendations

# Version 2
def top_recommended_movies_abs(user_id, user_item_matrix, user_similarity, num_recommendations,most_similar):
    predicted_ratings = []

    unrated_movies = user_item_matrix.columns[user_item_matrix.loc[user_id].isnull()]

    for item_id in unrated_movies:
        predicted_rating = predict_rating_with_abs(user_id, item_id, user_item_matrix, user_similarity,most_similar)
        predicted_ratings.append((item_id, predicted_rating))

    top_recommendations = sorted(predicted_ratings, key=lambda x: x[1], reverse=True)[:num_recommendations]

    return top_recommendations
