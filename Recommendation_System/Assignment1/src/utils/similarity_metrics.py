'''
A collection of functions for computing the similarity between users
'''
import numpy as np

# Pearson similarity
def pearson_correlation(user1_ratings, user2_ratings):
    # Exclude NaN values
    common_movies = user1_ratings.dropna().index.intersection(user2_ratings.dropna().index)
    if len(common_movies) == 0:
        return 0  # No common movies, return 0 correlation
    else:
        user1_common_ratings = user1_ratings[common_movies]
        user2_common_ratings = user2_ratings[common_movies]
        # Compute mean ratings
        mean_user1 = user1_ratings.mean()
        mean_user2 = user2_ratings.mean()
        # Compute numerator and denominators
        numerator = ((user1_common_ratings - mean_user1) * (user2_common_ratings - mean_user2)).sum()
        denominator1 = np.sqrt(((user1_common_ratings - mean_user1)**2).sum())
        denominator2 = np.sqrt(((user2_common_ratings - mean_user2)**2).sum())
        # Handle division by zero
        if denominator1 == 0 or denominator2 == 0:
            return 0
        else:
            return numerator / (denominator1 * denominator2)

# Compute mean and standard deviation as specified in the ITR formula 
def compute_user_mean_and_std(user_ratings,union_items):
    # Seleziona le valutazioni degli elementi comuni per entrambi gli utenti
    user_ratings_common = user_ratings.loc[union_items]
    
    n = len(user_ratings_common)
    m = len(user_ratings.dropna())

    mean_rating = np.sum(user_ratings.dropna())/n

    std_dev = np.sqrt((np.sum((user_ratings.dropna() - mean_rating)** 2)) /m)

    return mean_rating,std_dev

# URP similarity
def sim_urp(mean_rating_u,mean_rating_v,std_dev_u,std_dev_v):
    similarity_urp = 1 - (1 / (1 + np.exp(-np.abs(mean_rating_u - mean_rating_v) * np.abs(std_dev_u - std_dev_v))))
    return similarity_urp

# TRIANGLE similarity
def sim_triangle(user_u_ratings, user_v_ratings, union_items):
    
    if len(union_items) == 0:
        return 0.0
    
    u_ratings = user_u_ratings.loc[union_items]
    v_ratings = user_v_ratings.loc[union_items]
    
    u_ratings = np.nan_to_num(u_ratings, nan=0)
    v_ratings = np.nan_to_num(v_ratings, nan=0)
    
    numerator = np.sqrt(np.sum((u_ratings - v_ratings) ** 2))
    
    denominator = np.sqrt(np.sum(u_ratings ** 2)) + np.sqrt(np.sum(v_ratings ** 2))
    
    similarity = 1 - (numerator / denominator)
    
    return similarity

# Improved Triangle Similarity
def sim_itr(user_u_ratings, user_v_ratings):
    union_items = np.union1d(user_u_ratings.dropna().index, user_v_ratings.dropna().index)
    
    if len(union_items) == 0:
        return 0.0

    mean_rating_u, std_dev_u = compute_user_mean_and_std(user_u_ratings,union_items)
    mean_rating_v, std_dev_v = compute_user_mean_and_std(user_v_ratings,union_items)

    similarity_triangle = sim_triangle(user_u_ratings, user_v_ratings, union_items)
    similarity_urp = sim_urp(mean_rating_u, mean_rating_v, std_dev_u, std_dev_v)
    
    return similarity_triangle * similarity_urp

# Calculate the Pearson similarity between all pairs of users
def compute_user_similarity_with_pearson_correlation_all_users(user_item_matrix):
    user_similarity = {}

    for user_id_a in user_item_matrix.index:
        user_similarity[user_id_a] = {}
        for user_id_b in user_item_matrix.index:

            user_ratings_1 = user_item_matrix.loc[user_id_a]
            user_ratings_2 = user_item_matrix.loc[user_id_b]
            
            similarity = pearson_correlation(user_ratings_1, user_ratings_2)
            user_similarity[user_id_a][user_id_b] = similarity

    return user_similarity

# Calculate the ITR similarity between all pairs of users
def compute_user_similarity_with_ITR_all_users(user_item_matrix):
    user_similarity = {}

    for user_id_a in user_item_matrix.index:
        user_similarity[user_id_a] = {}
        for user_id_b in user_item_matrix.index:

            user_ratings_1 = user_item_matrix.loc[user_id_a]
            user_ratings_2 = user_item_matrix.loc[user_id_b]
            
            similarity = sim_itr(user_ratings_1, user_ratings_2)
            user_similarity[user_id_a][user_id_b] = similarity

    return user_similarity