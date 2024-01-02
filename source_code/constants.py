from enum import Enum
import os

#Large Dataset ml-latest
pickle_folder_path = 'pickle_files'
os.makedirs(pickle_folder_path, exist_ok=True)
users_ratings_matrix_pkl = os.path.join(pickle_folder_path, 'users_movies_ratings_matrix.pkl')
movies_ratings_matrix_pkl = os.path.join(pickle_folder_path, 'movies_users_ratings_matrix.pkl')
tag_scores_pkl = os.path.join(pickle_folder_path, 'tag_score_file.pkl')
movies_dict_pkl = os.path.join(pickle_folder_path, 'movies_dict.pkl')
tfidf_vectors_pkl = os.path.join(pickle_folder_path, 'tfidf_vectors.pkl')


#100k Dataset ml-100
pickle_folder_path_100 = 'pickle_files_100'
os.makedirs(pickle_folder_path_100 , exist_ok=True)
users_ratings_matrix_pkl_100  = os.path.join(pickle_folder_path_100, 'users_movies_ratings_matrix_100.pkl')
movies_ratings_matrix_pkl_100  = os.path.join(pickle_folder_path_100, 'movies_users_ratings_matrix_100.pkl')
movies_dict_pkl_100  = os.path.join(pickle_folder_path_100, 'movies_dict_100.pkl')
tfidf_vectors_pkl_100 = os.path.join(pickle_folder_path_100, 'tfidf_vectors_100.pkl')


class Constants(Enum):
    K = 128
    K_100 = 25
    
