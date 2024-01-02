import argparse
import os
import pickle
import pandas as pd

from .algorithms import *
from .similarities import *
from .utility import *



def main():
    parser = argparse.ArgumentParser(description='Recommender System')
    parser.add_argument('-n', '--num_recommendations', type=int, required=True, help='Number of recommendations')
    parser.add_argument('-s', '--similarity_metric', required=True, choices=['jaccard', 'dice', 'cosine', 'pearson'],
                        help='Similarity metric')
    parser.add_argument('-a', '--algorithm', required=True, choices=['user', 'item', 'tag', 'title', 'hybrid'],
                        help='Recommendation algorithm')
    parser.add_argument('-i', '--input', required=True, help='Input for recommendations')

    args = parser.parse_args()

    # Args
    num_recommendations_arg = int(args.num_recommendations)
    similarity_arg = args.similarity_metric
    algorithm_arg = args.algorithm
    input_id = int(args.input)

    try:
        with open(users_ratings_matrix_pkl, 'rb') as file:
            users_ratings_matrix = pickle.load(file)
        with open(movies_ratings_matrix_pkl, 'rb') as file:
            movies_ratings_matrix = pickle.load(file)
        with open(tag_scores_pkl, 'rb') as file:
            tag_score_vectors = pickle.load(file)
        with open(movies_dict_pkl, 'rb') as file:
            movies_dict = pickle.load(file)
        with open(tfidf_vectors_pkl, 'rb') as file:
            tfidf_vectors = pickle.load(file)
    except FileNotFoundError:
        print('Please Run preprocess -d "data_path" ')

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
        'tag': tag_based_recommendation,
        'hybrid': hybrid_recommendation,
        'title':content_based_recommendation
    }

    similarity_function = similarity_function_dict[similarity_arg]
    algorithm_function = algorithm_function_dict[algorithm_arg]
    
    recommendations = algorithm_function(input_id,
                                         users_ratings_matrix,
                                         movies_ratings_matrix,
                                         movies_dict,
                                         tag_score_vectors,
                                         tfidf_vectors,
                                         similarity_function,
                                         num_recommendations_arg,
                                         Constants.K.value)
    
    
    for recommendation_score, movie_id in sorted(recommendations, key=lambda x: (x[0], x[1]), reverse=True):
        # print(f'MovieId:{movie_id:6d}, Score:{recommendation_score}, Title: {movies_dict[movie_id]}')
        print(f'MovieId:{movie_id:6d}, Title: {movies_dict[movie_id]}')

if __name__ == '__main__':
    main()
