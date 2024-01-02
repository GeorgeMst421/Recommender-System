import pandas as pd
import re, math , json


def create_user_movie_ratings_matrix(ratings: pd.DataFrame):
    user_col = next((col for col in ['userId', 'user_id'] if col in ratings.columns), None)
    movie_col = next((col for col in ['movieId', 'item_id', 'movie_id'] if col in ratings.columns), None)
    rating_col = next((col for col in ['rating', 'ratings'] if col in ratings.columns), None)

    if user_col is None or movie_col is None or rating_col is None:
        raise ValueError("Could not determine column names for userId, movieId, or rating.")

    user_movie_ratings = {}
    movie_user_ratings = {}

    for index, row in ratings.iterrows():
        user_id = int(row[user_col])
        movie_id = int(row[movie_col])
        rating = float(row[rating_col])

        if user_id not in user_movie_ratings:
            user_movie_ratings[user_id] = {}
        user_movie_ratings[user_id][movie_id] = rating

        if movie_id not in movie_user_ratings:
            movie_user_ratings[movie_id] = {}

        movie_user_ratings[movie_id][user_id] = rating

    return user_movie_ratings, movie_user_ratings


def create_tag_vectors(tag_scores_df: pd.DataFrame):
    vectors = {}
    for index, row in tag_scores_df.iterrows():
        movie_id = int(row['movieId'])
        tag_id = int(row['tagId'])
        relevance = float(row['relevance'])

        if movie_id not in vectors:
            vectors[movie_id] = {}

        vectors[movie_id][tag_id] = relevance 

    return vectors


def clean_movie_titles(movies_dict: dict):
    cleaned_movies_dict = {movie_id: re.sub(r'\([^)]*\)', '', title).strip() for movie_id, title in movies_dict.items()}
    return cleaned_movies_dict

def custom_tokenize(text):
    #regular expression to find alphanumeric words
    return re.findall(r'\b\w+\b', text.lower())

def create_vocabulary(movies_dict: dict):
    vocabulary = set()
    for movie_title in movies_dict.values():
        tokens = custom_tokenize(movie_title)
        vocabulary.update(tokens)
    return vocabulary

def create_idf_vector(movies_dict, vocabulary):
    # First Calculate the DF
    df = {word: 0 for word in vocabulary}
    for movie_title in movies_dict.values():
        tokens = set(custom_tokenize(movie_title))
        for word in tokens:
            df[word] += 1
    
    # Then the IDF
    num_documents = len(movies_dict)
    idf = {word: math.log(num_documents / (df[word] + 1)) for word in vocabulary} #(+1) might not be needed in the numerator
    return idf



def create_tfidf_vectors(movies_dict):
    cleaned_movies_dict = clean_movie_titles(movies_dict) # Clean the titles from the release date in the parenthesis
    vocabulary = create_vocabulary(cleaned_movies_dict)  # Create the vocabulary
    idf_vector = create_idf_vector(cleaned_movies_dict, vocabulary) # Create the tfidf vector for each movie
   
    tfidf_vectors = {}
    for movie_id, title in cleaned_movies_dict.items():
        if movie_id not in tfidf_vectors:
            tfidf_vectors[movie_id] = {}
        tokens = custom_tokenize(title)
        tfidf_values = {word: tokens.count(word) * idf_vector[word] for word in tokens} 
        tfidf_vectors[movie_id] = tfidf_values

    return tfidf_vectors



def print_dict_as_json(my_dict):
    # Convert the dictionary to a JSON-formatted string
    json_str = json.dumps(my_dict, indent=2)

    # Print the JSON string
    print(json_str)





