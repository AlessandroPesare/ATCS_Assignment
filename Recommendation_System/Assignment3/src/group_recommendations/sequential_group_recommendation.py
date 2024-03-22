# SEQUENTIAL GROUP RECOMMENDATION 
import sys
import os

utils_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'utils'))
sys.path.append(utils_path)

import numpy as np
import pandas as pd
from predict_ratings import predict_rating, predict_rating_with_abs
from group_recommendations.disagreement_based import group_recommendation_disagreement_based
from group_recommendations.aggregation_based import hybrid_aggregation

def sequential_group_recommendation_aggregation_based(group_users, individual_recommendations, user_item_matrix, iterations):
    """
    Perform sequential group recommendation with dynamic alpha update.
    Parameters:
    group_users (List[str]): List of user IDs in the group.
    individual_recommendations (Dict[str, List[Tuple[str, float]]]): Dictionary mapping each user to a list of recommended movies with scores.
    user_item_matrix (DataFrame): DataFrame where user_item_matrix.loc[i][j] represents the rating of user i on item j.
    iterations (int): Number of iterations to run the sequential recommendation algorithm.
    Returns:
    A list of tuples containing movie IDs and their corresponding hybrid scores after the specified number of iterations.
    """
    # Initialize previous group satisfaction to None
    prev_group_recommendations = None
    
    # Perform sequential recommendation for the specified number of iterations
    for i in range(iterations):
        # Perform hybrid aggregation with updated alfa_j
        recommended_movies = hybrid_aggregation(group_users, individual_recommendations,prev_group_recommendations,user_item_matrix)
        # Update previous group satisfaction for next iteration
        prev_group_recommendations = recommended_movies
        print("Iterazione corrente:")
        print(recommended_movies[:10])
    
    return recommended_movies[:10]
'''
def sequential_group_recommendation_disagreement_based(group_users, individual_recommendations, user_item_matrix, iterations):
    """
    Perform sequential group recommendation with dynamic alpha update.
    Parameters:
    group_users (List[str]): List of user IDs in the group.
    individual_recommendations (Dict[str, List[Tuple[str, float]]]): Dictionary mapping each user to a list of recommended movies with scores.
    user_item_matrix (DataFrame): DataFrame where user_item_matrix.loc[i][j] represents the rating of user i on item j.
    iterations (int): Number of iterations to run the sequential recommendation algorithm.
    Returns:
    A list of tuples containing movie IDs and their corresponding hybrid scores after the specified number of iterations.
    """
    # Initialize previous group satisfaction to None
    prev_group_satisfaction = None
    
    # Perform sequential recommendation for the specified number of iterations
    for i in range(iterations):
        # Perform hybrid aggregation with updated alfa_j
        recommended_movies = hybrid_aggregation(group_users, individual_recommendations, user_item_matrix, prev_group_satisfaction)
        
        # Update previous group satisfaction for next iteration
        prev_group_satisfaction = calculate_group_satisfaction(group_users, recommended_movies)
    
    return recommended_movies
    '''