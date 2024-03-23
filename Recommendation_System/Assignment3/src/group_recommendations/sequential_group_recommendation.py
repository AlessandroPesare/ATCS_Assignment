# SEQUENTIAL GROUP RECOMMENDATION 
import sys
import os

utils_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'utils'))
group_racommendations_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'group_racommendations'))
sys.path.append(utils_path)
sys.path.append(group_racommendations_path)

import numpy as np
import pandas as pd
from predict_ratings import predict_rating, predict_rating_with_abs
from group_recommendations.disagreement_based import group_recommendation_disagreement_based
from group_recommendations.aggregation_based import hybrid_aggregation

def sequential_group_recommendation_aggregation_based(group_users, individual_recommendations, user_item_matrix, iterations):
    """
    Perform sequential group recommendation with dynamic alpha update.
    Parameters:
    group_users: List of user IDs in the group.
    individual_recommendations (Dict[str, List[Tuple[str, float]]]): Dictionary mapping each user to a list of recommended movies with scores.
    user_item_matrix (DataFrame): DataFrame where user_item_matrix.loc[i][j] represents the rating of user i on item j.
    iterations (int): Number of iterations to run the sequential recommendation algorithm.
    Returns:
    A list of tuples containing movie IDs and their corresponding hybrid scores after the specified number of iterations.
    """
    # Initialize previous group satisfaction to None
    prev_group_recommendations = []
    
    # Perform sequential recommendation for the specified number of iterations
    for i in range(iterations):
        # Perform hybrid aggregation with updated alfa_j
        recommended_movies = hybrid_aggregation(group_users, individual_recommendations,prev_group_recommendations,user_item_matrix)
        # Update previous group satisfaction for next iteration
        
        prev_group_recommendations += recommended_movies[:10]
        print("Iterazione corrente:")
        print(recommended_movies[:10])
    
    return recommended_movies[:10]

def sequential_group_recommendation_disagreement_based(group_users, individual_recommendations, user_item_matrix, similarities, iterations):
    """
    Perform sequential group recommendation with dynamic alpha update.
    Parameters:
    group_users: List of user IDs in the group.
    individual_recommendations (Dict[str, List[Tuple[str, float]]]): Dictionary mapping each user to a list of recommended movies with scores.
    user_item_matrix (DataFrame): DataFrame where user_item_matrix.loc[i][j] represents the rating of user i on item j.
    iterations (int): Number of iterations to run the sequential recommendation algorithm.
    Returns:
    A list of tuples containing movie IDs and their corresponding hybrid scores after the specified number of iterations.
    """
    # Initialize previous group satisfaction to None
    prev_group_satisfaction = []
    
    # Perform sequential recommendation for the specified number of iterations
    for i in range(iterations):

        recommended_movies = group_recommendation_disagreement_based(group_users,user_item_matrix, individual_recommendations,'mean_squared_difference',10, prev_group_satisfaction,1.2)
        # Update previous group satisfaction for next iteration
        prev_group_satisfaction += recommended_movies
        
        top_movies = []
        users_similarity = similarities

        for movie_id, _ in recommended_movies:
            mean = 0
            for user in group_users:
                score = predict_rating_with_abs(user,movie_id,user_item_matrix,similarities,1)
                mean += score
            mean /= 3
            top_movies.append((movie_id,mean))

        print("Iterazione corrente:")
        print(top_movies[:10])

    return top_movies