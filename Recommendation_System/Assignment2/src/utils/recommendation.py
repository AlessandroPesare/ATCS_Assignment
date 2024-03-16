'''
Recommendation functions
'''
import numpy as np
import pandas as pd
from predict_rating import predict_rating,predict_rating_with_abs

# Version 1
def top_recommended_movies(user_id, user_item_matrix, user_similarity, num_recommendations, most_similar):

    predicted_ratings = []

    unrated_movies = user_item_matrix.columns[user_item_matrix.loc[user_id].isnull()]

    for item_id in unrated_movies:
        predicted_rating = predict_rating(user_id, item_id, user_item_matrix, user_similarity,most_similar)
        predicted_ratings.append((item_id, predicted_rating))

    top_recommendations = sorted(predicted_ratings, key=lambda x: x[1], reverse=True)[:num_recommendations]

    return top_recommendations