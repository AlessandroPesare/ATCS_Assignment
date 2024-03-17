'''
POINT A
Implement two well established aggregation methods for producing the group recommendations.
The first aggregation approach is the average method. The main idea behind this
approach is that all members are considered equals. So, the rating of an item for a group
of users will be given be averaging the scores of an item across all group members.
The second aggregation method is the least misery method, where one member can act
as a veto for the rest of the group. In this case, the rating of an item for a group of users is
computed as the minimum score assigned to that item in all group members
recommendations.
'''

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


def average_aggregation(group_users, individual_recommendations, user_item_matrix):
    """
    Calculate the average rating for each movie based on individual recommendations and user-item ratings.

    Parameters:
    group_users (list): List of user IDs in the group.
    individual_recommendations (dict): A dictionary mapping each user to a list of recommended movies with scores.
    user_item_matrix (DataFrame): DataFrame where user_item_matrix.loc[i][j] represents the rating of user i on item j.

    Returns:
    list: A list of tuples containing movie IDs and their corresponding average ratings, sorted by rating in descending order.
    """
    recommended_movies_with_scores = []
    users2movies_ratings = user_ratings(group_users,user_item_matrix)
    # Iterate over all movies
    for movie_id in user_item_matrix.columns:
        total_rating = 0
        total_users = 0
        # Calculate total rating and total users for the movie across all group members
        for user_id in group_users:
            recommendations = individual_recommendations[user_id]
            movies2ratings = users2movies_ratings[user_id]
            recommendations = recommendations + movies2ratings
            for recommendation in recommendations:
                if recommendation[0] == movie_id:
                    total_rating += recommendation[1]
                    total_users += 1
                    break
                
        # Calculate average rating for the movie
        if total_users > 0:
            average_rating = total_rating / total_users
            recommended_movies_with_scores.append((movie_id, average_rating))
    # Sort movies based on their average ratings
    sorted_movies = sorted(recommended_movies_with_scores, key=lambda x: x[1], reverse=True)
    
    return sorted_movies

def least_misery_aggregation(group_users, individual_recommendations, user_item_matrix):
    """
    Calculate the least misery aggregation of ratings for each movie across group members.

    Parameters:
    group_users (list): List of user IDs in the group.
    individual_recommendations (dict): A dictionary mapping each user to a list of recommended movies with scores.
    user_item_matrix (DataFrame): DataFrame where user_item_matrix.loc[i][j] represents the rating of user i on item j.

    Returns:
    list: A list of tuples containing movie IDs and their corresponding minimum ratings across group members, sorted by rating in descending order.
    """
    recommended_movies_with_scores = []
    users2movies_ratings = user_ratings(group_users,user_item_matrix)
    # Iterate over all movies
    for movie_id in user_item_matrix.columns:
        min_rating = float('inf')  # Initialize with positive infinity
        # Iterate over all users in the group
        for user_id in group_users:
            if user_id in individual_recommendations:
                recommendations = individual_recommendations[user_id]
                movies2ratings = users2movies_ratings[user_id]
                recommendations = recommendations + movies2ratings
                for recommendation in recommendations:
                    if recommendation[0] == movie_id:
                        min_rating = min(min_rating, recommendation[1])  # Update minimum rating
                        break  # No need to continue searching once found
        # Add movie and minimum rating to recommended movies list
        if min_rating != float('inf'):  # Check if any rating was found for the movie
            recommended_movies_with_scores.append((movie_id, min_rating))
    # Sort movies based on their minimum ratings
    sorted_movies = sorted(recommended_movies_with_scores, key=lambda x: x[1],reverse=True)

    return sorted_movies