import os
import argparse
import pandas as pd
import pickle
from .utility import *
from .constants import *


def preprocess():
    
    parser = argparse.ArgumentParser(description='Recommender System')
    parser.add_argument('-d', '--data_directory', required=True, help='Directory of full dataset')

    args = parser.parse_args()
    data_directory = args.data_directory

     # Files
    genome_scores_file = os.path.join(data_directory, 'genome-scores.csv')
    genome_tags_file = os.path.join(data_directory, 'genome-tags.csv')
    links_file = os.path.join(data_directory, 'links.csv')
    movies_file = os.path.join(data_directory, 'movies.csv')
    ratings_file = os.path.join(data_directory, 'ratings.csv')
    tags_file = os.path.join(data_directory, 'tags.csv')

    # DataFrames
    genome_scores_df = pd.read_csv(genome_scores_file)
    genome_tags_df = pd.read_csv(genome_tags_file)
    links_df = pd.read_csv(links_file)
    movies_df = pd.read_csv(movies_file)
    ratings_df = pd.read_csv(ratings_file)
    tags_df = pd.read_csv(tags_file)

    # Print the number of items in each csv
    print(f'genome-scores.csv : {len(genome_scores_df)}')
    print(f'genome-tags.csv   : {len(genome_tags_df)}')
    print(f'links.csv         : {len(links_df)}')
    print(f'movies.csv        : {len(movies_df)}')
    print(f'ratings.csv       : {len(ratings_df)}')
    print(f'tags.csv          : {len(tags_df)}')
    
    total_users = len(ratings_df['userId'].unique())
    total_movies =  len(movies_df['movieId'].unique())
    print(f'\nTotal Users: {total_users}\nTotal Movies: {total_movies}')


    print("Preprocessing....")
  
    # Matrices
    users_ratings_matrix, movies_ratings_matrix = create_user_movie_ratings_matrix(ratings_df)
   
    # Movie_ids-titles 
    movies_dict = movies_df.set_index('movieId')['title'].to_dict()
   
    # Calcualte the tag vectors
    tag_score_vectors = create_tag_vectors(genome_scores_df)
    
    # TFIDF Vectors
    tfidf_vectors = create_tfidf_vectors(movies_dict)

    with open(users_ratings_matrix_pkl, 'wb') as file:
        pickle.dump(users_ratings_matrix, file)
    with open(movies_ratings_matrix_pkl, 'wb') as file:
        pickle.dump(movies_ratings_matrix, file)
    with open(tag_scores_pkl, 'wb') as file:
        pickle.dump(tag_score_vectors, file)
    with open(movies_dict_pkl, 'wb') as file:
        pickle.dump(movies_dict, file)
    with open(tfidf_vectors_pkl, 'wb') as file:
        pickle.dump(tfidf_vectors, file)
   
    print('Preprocess Completed')





