import argparse, sys, os, pickle
import pandas as pd

from .algorithms import *
from .similarities import *
from .utility import *

#
# This file is the main for the 100k dataset
#

def main():
    parser = argparse.ArgumentParser(description='Recommender System')
    parser.add_argument('-n', '--num_recommendations', type=int, required=True, help='Number of recommendations')
    parser.add_argument('-s', '--similarity_metric', required=True, choices=['jaccard', 'dice', 'cosine', 'pearson'],
                        help='Similarity metric')
    parser.add_argument('-a', '--algorithm', required=True, choices=['user', 'item', 'title', 'hybrid'],
                        help='Recommendation algorithm')
    parser.add_argument('-i', '--input', required=True, help='Input for recommendations')

    args = parser.parse_args()

    # Args
    num_recommendations_arg = int(args.num_recommendations)
    similarity_arg = args.similarity_metric
    algorithm_arg = args.algorithm
    input_id = int(args.input)


    # Using Pickle for Matrices and Variables for some preprocessing calculations
    try:
        with open(users_ratings_matrix_pkl_100, 'rb') as file:
            users_ratings_matrix = pickle.load(file)
        with open(movies_ratings_matrix_pkl_100, 'rb') as file:
            movies_ratings_matrix = pickle.load(file)
        with open(movies_dict_pkl_100, 'rb') as file:
            movies_dict = pickle.load(file)
        with open(tfidf_vectors_pkl_100, 'rb') as file:
            tfidf_vectors = pickle.load(file)
    except FileNotFoundError:
        print("Please run preprocess_100 -d 'data-folder-path' ")
        sys.exit()

    # Two dicts implementing a switch case for the similarity and function argument
    similarity_function_dict = {
        'jaccard': jaccard_similarity,
        'dice': dice_similarity,
        'cosine': cosine_similarity,
        'pearson': pearson_similarity
    }
    algorithm_function_dict = {
        'user': user_user_recommendation,
        'item': item_item_recommendation,
        'title': content_based_recommendation,
        'hybrid': hybrid_recommendation
    }

    similarity_function = similarity_function_dict[similarity_arg]
    algorithm_function = algorithm_function_dict[algorithm_arg]

    recommendations = algorithm_function(input_id,
                                         users_ratings_matrix,
                                         movies_ratings_matrix,
                                         movies_dict,
                                         {},
                                         tfidf_vectors,
                                         similarity_function,
                                         num_recommendations_arg,
                                         Constants.K_100.value)

    
    for recommendation_score, movie_id in sorted(recommendations, key=lambda x: (x[0], x[1]), reverse=True):
        # print(f'MovieId:{movie_id:6d}, Score:{recommendation_score}, Title: {movies_dict[movie_id]}')
        print(f'MovieId:{movie_id:6d}, Title: {movies_dict[movie_id]}')


if __name__ == '__main__':
    main()
