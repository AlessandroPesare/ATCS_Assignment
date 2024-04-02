import numpy as np

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

def group_recommendation_disagreement_based(group_users, user_item_matrix, individual_recommendations, g='mean_squared_difference',top_n=10):
    """
    Generate group recommendation based on disagreement measure.

    Parameters:
    group_users: users in the group
    user_item_matrix: dataframe pansad where user_item_matrix.loc[i][j] represents the rating of user i on item j.
    g (str): Type of deviation function. 'mean_squared_difference' or 'mean_absolute_difference'.

    Returns:
    list: List of tuples containing (item_index, recommendation_score) for the top N recommended items.
    """
    disagreements = []
    for movie_id in user_item_matrix.columns:
        deviation = disagreement(group_users, user_item_matrix, individual_recommendations, movie_id, g)
        if deviation <= 0.2:  
            disagreements.append((movie_id, deviation))  
            
    top_disagreement_recommendations = sorted(disagreements, key=lambda x: x[1])

    top_mean_scores = []
    for movie_id, _ in top_disagreement_recommendations:
        mean_score = 0
        count = 0
        for user_id in group_users:
            for movie, score in individual_recommendations.get(user_id, []):
                if movie == movie_id:
                    mean_score += score
                    count += 1
        if count != 0:
            mean_score /= count
            top_mean_scores.append((movie_id, mean_score))

    top_n_recommendations = sorted(top_mean_scores, key=lambda x: x[1], reverse=True)[:top_n]
    return top_n_recommendations