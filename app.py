import streamlit as st
import pickle
import requests
import gzip

# Load the compressed 'similarity' object from the .gz file
with gzip.open('similarity.pkl.gz', 'rb') as f:
    similarity = pickle.load(f)

# Use st.cache_data to cache the API responses for poster fetching
@st.cache_data
def fetch_poster(movie_id):
    try:
        response = requests.get(
            f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=a941527f987115aa5364e9a8e72a9c42&language=en-US'
        )
        data = response.json()
        if 'poster_path' in data:
            return "https://image.tmdb.org/t/p/w500/" + data['poster_path']
        else:
            return "https://via.placeholder.com/500x750?text=No+Poster+Available"
    except Exception as e:
        return "https://via.placeholder.com/500x750?text=Error+Fetching+Poster"

# Recommend movies based on similarity
def recommend(movie_name):
    try:
        movie_index = movies[movies['title'] == movie_name].index[0]
        distances = similarity[movie_index]
        movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

        recommend_movies = []
        recommend_movies_posters = []
        for i in movies_list:
            movie_id = movies.iloc[i[0]].movie_id
            recommend_movies.append(movies.iloc[i[0]].title)
            recommend_movies_posters.append(fetch_poster(movie_id))
        return recommend_movies, recommend_movies_posters
    except IndexError:
        return [], []

# Load movie data
movies = pickle.load(open('movies.pkl', 'rb'))
movies_list = movies['title'].values

# Streamlit app UI
st.title('Movie Recommender System')

selected_movie_name = st.selectbox('Select a movie', movies_list)

if st.button('Recommend'):
    names, posters = recommend(selected_movie_name)

    if names:
        cols = st.columns(5)
        for i, col in enumerate(cols):
            with col:
                st.text(names[i])
                st.image(posters[i])
    else:
        st.error("Sorry, we couldn't find any recommendations for this movie.")
