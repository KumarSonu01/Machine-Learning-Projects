import pickle
import streamlit as st
import requests

# ---------- Day/Night Mode ----------
dark_mode = st.toggle("🌙 Dark Mode") if hasattr(st, "toggle") else st.checkbox("🌙 Dark Mode")

if dark_mode:
    st.markdown(
        """
        <style>
        .stApp {
            background-color: #0e1117;
            color: white;
        }
        .stSelectbox label, .stText, .stHeader, .stButton button {
            color: white !important;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
else:
    st.markdown(
        """
        <style>
        .stApp {
            background-color: #ffffff;
            color: black;
        }
        .stSelectbox label, .stText, .stHeader, .stButton button {
            color: black !important;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

# ---------- Poster Fetch ----------
def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=06b71def1b642d6dd2e01db6576eda1a&language=en-US"
    data = requests.get(url).json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

# ---------- Recommendation Function ----------
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

# ---------- Main App ----------
st.header('🎬 Movie Recommender System')
try:
    with open('movie_list.pkl','rb') as file:
        movies = pickle.load(file)
    with open('similarity.pkl','rb') as file:
        similarity = pickle.load(file)
except FileNotFoundError:
    st.error("Error: Files 'movie_list.pkl' or 'similarity.pkl' not found. Please ensure they exist in the same directory as app.py.")
else:
    movie_list = movies['title'].values
    selected_movie = st.selectbox("Type or select a movie from the dropdown", movie_list)

    if st.button('Show Recommendation'):
        recommended_movie_names, recommended_movie_posters = recommend(selected_movie)
        cols = st.columns(5)
        for i, col in enumerate(cols):
            with col:
                st.text(recommended_movie_names[i])
                st.image(recommended_movie_posters[i])

    st.text("Made with ❤️ by [Sonu Kumar]")
