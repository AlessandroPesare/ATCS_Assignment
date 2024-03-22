
def user_satisfaction(user_id, group_recommendations, individual_recommendations):
    """
    Calculate the satisfaction of a single user based on group recommendations and individual recommendations.

    Parameters:
    user_id (str): ID of the user.
    group_recommendations (list): List of recommended movies for the group.
    individual_recommendations (dict): A dictionary mapping each user to a list of recommended movies with scores.

    Returns:
    float: Satisfaction score of the user.
    """
    # Calculate group_list_sat
    group_list_sat = sum(score for movie, score in group_recommendations)

    # Calculate user_list_sat
    user_list_sat = sum(score for movie, score in individual_recommendations[user_id])

    # Calculate user satisfaction
    user_satisfaction_score = group_list_sat / user_list_sat if user_list_sat != 0 else -1

    return user_satisfaction_score
