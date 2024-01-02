import argparse, pickle
from .convertion_100 import *
from .utility import *
from .constants import *

#
# This file is used for preprocessing the data of the ml-100k dataset
#

def preprocess():
    print('Preprocessing')
    parser = argparse.ArgumentParser(description='Preprocess of Recommender System')
    parser.add_argument('-d', '--data_directory', required=True, help='Directory of 100k dataset')
    args = parser.parse_args()

    #Convert the files to csv
    data_directory = args.data_directory
    convert(data_directory)

    #Read the csv's
    ratings_df = pd.read_csv('converted_csv/u_data.csv').sort_values(by=['user_id', 'item_id'])
    movies_df = pd.read_csv('converted_csv/u_item.csv', header=None, usecols=[0, 1])
    
    # Print the number of users and ratings
    total_users = len(ratings_df['user_id'].unique())
    total_movies = len(movies_df[1].unique())
    total_ratings = len(ratings_df)
    print(f'\nUsers: {total_users}\nMovies: {total_movies} \nRatings: {total_ratings}')

    #Create the Matrices and the Movie Dictionary
    users_ratings_matrix, movies_ratings_matrix = create_user_movie_ratings_matrix(ratings_df)
    movies_dict = movies_df.set_index(0)[1].to_dict()

    # TFIDF Vectors
    tfidf_vectors = create_tfidf_vectors(movies_dict) # Create the tfidf vector for each movie

    #Save them using pickle
    print("Preprocessing....")
    with open(users_ratings_matrix_pkl_100, 'wb') as file:
        pickle.dump(users_ratings_matrix, file)
    with open(movies_ratings_matrix_pkl_100, 'wb') as file:
        pickle.dump(movies_ratings_matrix, file)
    with open(movies_dict_pkl_100, 'wb') as file:
        pickle.dump(movies_dict, file)
    with open(tfidf_vectors_pkl_100, 'wb') as file:
        pickle.dump(tfidf_vectors, file)

    print('\nPreprocess Completed')


