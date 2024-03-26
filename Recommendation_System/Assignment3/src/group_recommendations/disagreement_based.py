
import sys
import os

utils_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'utils'))

sys.path.append(utils_path)
import numpy as np
from predict_ratings import user_ratings


def disagreement(group_users, user_item_matrix,individual_recommendations,movie_id, g='mean_squared_difference'):
    """
    Compute disagreement of a group on movie.
    Return: Disagreement value.
    """
    ratings = []

    for user in group_users:
        if not np.isnan(user_item_matrix.loc[user][movie_id]):
            ratings.append(user_item_matrix.loc[user][movie_id])
        else:
            movie_score = {movie_id: score for movie_id, score in individual_recommendations[user]}
            ratings.append(movie_score[movie_id])

    group_avg = np.mean(ratings)

    if g == 'mean_squared_difference':
        deviation = np.mean([(r - group_avg) ** 2 for r in ratings])
    elif g == 'mean_absolute_difference':
        deviation = np.mean([np.abs(r - group_avg) for r in ratings])
    else:
        raise ValueError("Invalid deviation function type.")

    return deviation

def group_recommendation_disagreement_based(group_users,individual_recommendations,user_item_matrix,prev_group_recommendations,users_satisfaction,top_n,g,increase_factor):
    """
    Generate group recommendation based on disagreement measure.

    Parameters:
    group_users: users in the group
    user_item_matrix: dataframe pandas where user_item_matrix.loc[i][j] represents the rating of user i on item j.
    g (str): Type of deviation function. 'mean_squared_difference' or 'mean_absolute_difference'.
    top_n (int): Number of top recommendations to return.
    prev_group_recommendations: Recommendations from the previous iteration.
    increase_factor (float): Factor by which to increase the score of movies liked by the least satisfied user.

    Returns:
    list: List of tuples containing (item_index, recommendation_score) for the top N recommended items.
    """
    disagreements = []
    for movie_id in user_item_matrix.columns:
        deviation = disagreement(group_users, user_item_matrix, individual_recommendations, movie_id, g)
        if deviation <= 0.3:  
            disagreements.append((movie_id, deviation))  
    top_disagreement_recommendations = sorted(disagreements, key=lambda x: x[1])

    least_satisfied_users = []
    recommended_movies_with_scores = []
    users2movies_ratings = user_ratings(group_users, user_item_matrix)


    # Step 1: Calculate average user satisfaction in the group in the previous iteration
    if prev_group_recommendations:
        max_satisfaction = max(users_satisfaction.values())
        min_satisfaction = min(users_satisfaction.values())
        alfa_j = max_satisfaction - min_satisfaction
        print(alfa_j)
        avg_user_satisfaction = sum(users_satisfaction[user_id] for user_id in group_users) / len(group_users)
        least_satisfied_users = [user_id for user_id in group_users if users_satisfaction[user_id] < avg_user_satisfaction]

    # Step 2: Generate recommendations
    for movie_id, _ in top_disagreement_recommendations:
        mean_score = 0
        count = 0
        for user_id in group_users:
            recommendations = individual_recommendations[user_id]
            movies2ratings = users2movies_ratings[user_id]
            recommendations = recommendations + movies2ratings
            for recommendation in recommendations:
                if recommendation[0] == movie_id:
                    if user_id in least_satisfied_users:
                        mean_score += recommendation[1] * increase_factor
                    else:
                        mean_score += recommendation[1]
                    count += 1
                    break
        if count != 0:
            mean_score /= count
            found = False
            for movie, _ in prev_group_recommendations:
                if movie == movie_id:
                    found = True
                    break
            if not found:
                recommended_movies_with_scores.append((movie_id, mean_score))
    # Step 3: Select top recommendations
    top_n_recommendations = sorted(recommended_movies_with_scores, key=lambda x: x[1], reverse=True)

    return top_n_recommendations[:top_n]