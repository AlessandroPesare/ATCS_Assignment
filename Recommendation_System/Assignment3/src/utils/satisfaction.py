# USER SATISFACTION
import sys
import os

utils_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'utils'))
sys.path.append(utils_path)
from predict_ratings import predict_rating_with_abs

def user_satisfaction(user_id,individual_recommendations,group_recommendations,user_item_matrix,similarities):
    """
    Calculate the satisfaction of a single user based on group recommendations and individual recommendations.

    Parameters:
    user_id (str): ID of the user.
    group_recommendations (list): List of recommended movies for the group.
    individual_recommendations (dict): A dictionary mapping each user to a list of recommended movies with scores.

    Returns:
    float: Satisfaction score of the user.
    """
    group_list_sat = 0
    # Calculate group_list_sat
    for movie_id, _ in group_recommendations[:10]:
            score = predict_rating_with_abs(user_id,movie_id,user_item_matrix,similarities,1)
            group_list_sat += score

    # Calculate user_list_sat
    user_list_sat = sum(score for movie, score in individual_recommendations[user_id][:10])

    # Calculate user satisfaction
    user_satisfaction_score = group_list_sat / user_list_sat if user_list_sat != 0 else -1

    return user_satisfaction_score
