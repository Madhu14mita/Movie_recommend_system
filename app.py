import pickle
import gdown
import os
import streamlit as st
import requests

# --- Google Drive File IDs ---
movie_file_id = '1bLWry5CTJjTiXsqceReGB42s3VZyFg2e'
similarity_file_id = '1UVHVD5VdKAhwEnUoTMCBCmL2zK0sKvuq'

# --- Download files if not already present ---
if not os.path.exists("movie.pkl"):
    gdown.download(f"https://drive.google.com/uc?id={movie_file_id}", "movie.pkl", quiet=False)

if not os.path.exists("similarity.pkl"):
    gdown.download(f"https://drive.google.com/uc?id={similarity_file_id}", "similarity.pkl", quiet=False)

# --- Load the pickle files ---
with open("movie.pkl", "rb") as f:
    movies = pickle.load(f)

with open("similarity.pkl", "rb") as f:
    similarity = pickle.load(f)


# ---- Streamlit UI ----
st.header('Movie Recommender System Using Machine Learning')

def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US"
    data = requests.get(url).json()
    poster_path = data.get('poster_path')
    if poster_path:
        return f"https://image.tmdb.org/t/p/w500/{poster_path}"
    return ""

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)
    return recommended_movie_names, recommended_movie_posters

movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

if st.button('Show Recommendation'):
    recommended_movie_names, recommended_movie_posters = recommend(selected_movie)
    cols = st.columns(5)
    for idx, col in enumerate(cols):
        with col:
            st.text(recommended_movie_names[idx])
            st.image(recommended_movie_posters[idx])
