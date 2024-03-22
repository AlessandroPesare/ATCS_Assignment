# USER SATISFACTION

def user_satisfaction(user_id,individual_recommendations,group_recommendations):
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
    for movie_group, _ in group_recommendations[:10]:
        for movie_id, score in individual_recommendations[user_id]:
            if movie_group == movie_id:
                group_list_sat += score

    # Calculate user_list_sat
    user_list_sat = sum(score for movie, score in individual_recommendations[user_id][:10])

    # Calculate user satisfaction
    user_satisfaction_score = group_list_sat / user_list_sat if user_list_sat != 0 else -1

    return user_satisfaction_score
