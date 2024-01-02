import heapq
import sys
import numpy as np
from .constants import *
from .utility import *


def user_user_recommendation(user_id: int,
                             users_ratings_matrix: dict[int: float],
                             movies_ratings_matrix: dict[int: dict[int: float]],
                             movies_dict: dict[int: str],
                             tag_score_vectors,
                             tfidf_vectors,
                             similarity_function: callable,
                             number_of_recommendations: int,
                             K_VALUE: int):
    recommendations = []
    try:
        user_ratings = users_ratings_matrix[user_id]
    except KeyError:
        print(f'User with id: {user_id} does not exist')
        sys.exit()

    # Find all the unwatched movies of target user
    unwatched_movies = [movie_id for movie_id in movies_dict.keys() if movie_id not in user_ratings]
    print(f'Number of unwatched movies for user {user_id}: {len(unwatched_movies)}')

    # Calculate the similarities between the target user and the users who have at least one common movie rated
    similarities = {}
    for other_user_id, other_ratings in users_ratings_matrix.items():
        if other_user_id != user_id:
            similarity = round(similarity_function(user_ratings, other_ratings), 2)
            similarities[other_user_id] = similarity
            if similarity > 1 or similarity < -1:
                print(f'Error for users:{user_id}, {other_user_id} : similarity:{similarity}') 

    print('User User Running')
    for movie_id in unwatched_movies:

        if movie_id not in movies_ratings_matrix or len(movies_ratings_matrix[movie_id]) < K_VALUE:
            continue

        similar_users = []
        for other_user_id in users_ratings_matrix:
            if user_id != other_user_id and movie_id in users_ratings_matrix[other_user_id] and other_user_id in similarities:
                similarity = similarities[other_user_id]
                if similarity < 0:
                    continue
                rating = users_ratings_matrix[other_user_id][movie_id]
                if len(similar_users) < Constants.K.value:
                    heapq.heappush(similar_users, (similarity, rating))
                else:
                    heapq.heappushpop(similar_users, (similarity, rating))

        # Calculating the recommendation score
        numerator = sum((similarity * rating) for similarity, rating in similar_users)
        denominator = sum(similarity for similarity, _ in similar_users)
        score = round((numerator / denominator if denominator != 0 else 0.0), 1)

        if score > 5.0 or score < 0:
            print(f"Error for movie id {movie_id}, score: {score}")
        else:
            score_movie_tuple = (score, movie_id)
            if len(recommendations) < number_of_recommendations:
                heapq.heappush(recommendations, score_movie_tuple)
            else:
                heapq.heappushpop(recommendations, score_movie_tuple)

    return recommendations


def item_item_recommendation(user_id: int,
                             users_ratings_matrix: dict[int: float],
                             movies_ratings_matrix: dict[int: dict[int: float]],
                             movies_dict: dict[int: str],
                             tag_score_vectors,
                             tfidf_vectors,
                             similarity_function: callable,
                             number_of_recommendations: int,
                             K_VALUE: int):
    try:
        user_ratings = users_ratings_matrix[user_id]
    except KeyError:
        print(f'User with id: {user_id} does not exist')
        sys.exit()
    
    recommendations = []

    unwatched_movies = [movie_id for movie_id in movies_dict if movie_id not in user_ratings]
    print(f'Number of unwatched movies for user {user_id}: {len(unwatched_movies)}')

    print('Item Item Running')
    for movie_id in unwatched_movies:
        unwatched_movie_dict = movies_ratings_matrix.get(movie_id, {})
        if not unwatched_movie_dict or len(unwatched_movie_dict) < K_VALUE:
            continue

        similar_movies = []
        for other_movie_id in user_ratings:
            watched_movie_dict = movies_ratings_matrix[other_movie_id]
            similarity = similarity_function(unwatched_movie_dict, watched_movie_dict)
            if similarity < 0:
                continue
            rating = user_ratings[other_movie_id]
            if len(similar_movies) < Constants.K.value:
                heapq.heappush(similar_movies, (similarity, rating))
            else:
                heapq.heappushpop(similar_movies, (similarity, rating))

        numerator = sum(similarity * rating for similarity, rating in similar_movies)
        denominator = sum(similarity for similarity, _ in similar_movies)
        score = round((numerator / denominator if denominator != 0 else 0.0), 1)

        if score > 5.0 or score < 0:
            print(f"Error for movie id {movie_id}, score: {score}") 
        else:
            score_movie_tuple = (score, movie_id)
            if len(recommendations) < number_of_recommendations:
                heapq.heappush(recommendations, score_movie_tuple)
            else:
                heapq.heappushpop(recommendations, score_movie_tuple)

    return recommendations


def tag_based_recommendation(input_movie_id: int,
                             users_ratings_matrix: dict[int: float],
                             movies_ratings_matrix: dict[int: dict[int: float]],
                             movies_dict: dict[int: str],
                             tag_score_vectors,
                             tfidf_vectors,
                             similarity_function: callable,
                             number_of_recommendations: int,
                             K_VALUE: int):
    similar_movies = []
    try:
        vector_1 = tag_score_vectors[input_movie_id]
    except KeyError:
        print(f'Movie with id: {input_movie_id} does not exist / has no tags ')
        sys.exit() 

    print(f'Target Movie: {movies_dict[input_movie_id]}')
    for other_movie_id in tag_score_vectors:
        if other_movie_id != input_movie_id:
            vector_2 = tag_score_vectors[other_movie_id]        
            similarity = similarity_function(vector_1, vector_2)
            
            if len(similar_movies) < K_VALUE:
                heapq.heappush(similar_movies, (similarity, other_movie_id))
            else:
                heapq.heappushpop(similar_movies, (similarity, other_movie_id))

    return heapq.nlargest(number_of_recommendations, similar_movies)



def hybrid_recommendation(user_id: int,
                             users_ratings_matrix: dict[int: float],
                             movies_ratings_matrix: dict[int: dict[int: float]],
                             movies_dict: dict[int: str],
                             tag_score_vectors,
                             tfidf_vectors,
                             similarity_function: callable,
                             number_of_recommendations: int,
                             K_VALUE: int):
    
    # Calculate recommendations from User-User Algorithm
    user_recommendations = user_user_recommendation(user_id,
                                                    users_ratings_matrix,
                                                    movies_ratings_matrix,
                                                    movies_dict,
                                                    tag_score_vectors,
                                                    tfidf_vectors,
                                                    similarity_function,
                                                    number_of_recommendations,
                                                    K_VALUE)

    # Calculate recommendations from Item-Item Algorithm
    item_recommendations = item_item_recommendation(user_id,
                                                    users_ratings_matrix,
                                                    movies_ratings_matrix,
                                                    movies_dict,
                                                    tag_score_vectors,
                                                    tfidf_vectors,
                                                    similarity_function,
                                                    number_of_recommendations,
                                                    K_VALUE)
    

    # Merge the results
    movie_ids = set()
    for _, movie_id in user_recommendations + item_recommendations:
        movie_ids.add(movie_id)

    # Calculate the final recommendations
    recommendations = set()
    for movie_id in movie_ids:
        tag_rec_list = content_based_recommendation(movie_id,
                                                users_ratings_matrix,
                                                movies_ratings_matrix,
                                                movies_dict,
                                                tag_score_vectors,
                                                tfidf_vectors,
                                                similarity_function,
                                                number_of_recommendations,
                                                K_VALUE)
        for similarity, tag_movie_id in tag_rec_list:
            same_movie_tuple = [t for t in recommendations if t[1] == tag_movie_id] # Check if the movie id is already in the set
            if same_movie_tuple:
                mean = sum(t[0] for t in same_movie_tuple) / len(same_movie_tuple) #had to do it this way
                updated_tuple = (mean, tag_movie_id)
                recommendations.difference_update(same_movie_tuple)
                recommendations.add(updated_tuple)
            else:
                recommendations.add((similarity, tag_movie_id))
    return heapq.nlargest(number_of_recommendations, recommendations)

def content_based_recommendation(input_movie_id: int,
                             users_ratings_matrix,
                             movies_ratings_matrix,
                             movies_dict ,
                             tag_score_vectors,
                             tfidf_vectors: dict[int: dict[str: float]],
                             similarity_function: callable,
                             number_of_recommendations: int,
                             K_VALUE):
    input_movie_tfidf = tfidf_vectors[input_movie_id]

    recommendations = []
    for movie_id, tfidf in tfidf_vectors.items():
        if movie_id != input_movie_id:
            similarity = similarity_function(tfidf,input_movie_tfidf)
            if similarity < 0:
                continue
            if len(recommendations) < number_of_recommendations:
                heapq.heappush(recommendations, (similarity, movie_id)) 
            else:
                heapq.heappushpop(recommendations, (similarity, movie_id))

    return recommendations
