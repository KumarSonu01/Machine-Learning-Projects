import pickle
import streamlit as st
import requests

# ----------------- CONFIG -----------------
TMDB_API_KEY = "06b71def1b642d6dd2e01db6576eda1a"   # your TMDB key
YOUTUBE_API_KEY = "AIzaSyAokdZIbGxGPDytYo8fnb77DwVcAC2yP_c"  # your YouTube key

# ----------------- FUNCTIONS -----------------
def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={TMDB_API_KEY}&language=en-US"
    data = requests.get(url).json()

    # Handle missing poster safely
    if "poster_path" in data and data["poster_path"]:
        poster_path = data["poster_path"]
        full_path = "https://image.tmdb.org/t/p/w500" + poster_path
    else:
        full_path = "https://via.placeholder.com/500x750?text=No+Poster"

    title = data.get("title", "Unknown Title")
    return full_path, title

def fetch_trailer(title):
    search_url = (
        f"https://www.googleapis.com/youtube/v3/search?part=snippet&q={title} trailer&key={YOUTUBE_API_KEY}&maxResults=1"
    )
    response = requests.get(search_url).json()
    if "items" in response and len(response["items"]) > 0:
        video_id = response["items"][0]["id"]["videoId"]
        return f"https://www.youtube.com/watch?v={video_id}"
    return None

def recommend(movie):
    movie_index = movies[movies["title"] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(
        list(enumerate(distances)), reverse=True, key=lambda x: x[1]
    )[1:6]

    recommended_movies = []
    recommended_posters = []
    recommended_trailers = []

    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        poster, title = fetch_poster(movie_id)
        trailer = fetch_trailer(title)
        recommended_movies.append(title)
        recommended_posters.append(poster)
        recommended_trailers.append(trailer)

    return recommended_movies, recommended_posters, recommended_trailers

# ----------------- LOAD MODELS -----------------
movies = pickle.load(open("movie_list.pkl", "rb"))
similarity = pickle.load(open("similarity.pkl", "rb"))

# ----------------- STREAMLIT UI -----------------
st.set_page_config(page_title="Movie Recommender", layout="wide")

# Add Day/Night toggle
# Add Day/Night toggle
mode = st.sidebar.radio("🌙 Toggle Theme", ["Day Mode", "Night Mode"])

if mode == "Night Mode":
    st.markdown(
        """
        <style>
        .stApp {
            background-color: #121212;
            color: white;
        }
        .stButton>button {
            background-color: #444;
            color: white;
        }
        .stSelectbox, .stTextInput {
            background-color: #333 !important;
            color: white !important;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
else:
    st.markdown(
        """
        <style>
        .stApp {
            background-color: white;
            color: black;
        }
        .stButton>button {
            background-color: #ddd;
            color: black;
        }
        .stSelectbox, .stTextInput {
            background-color: #f9f9f9 !important;
            color: black !important;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


st.title("🎬 Movie Recommendation System")
selected_movie = st.selectbox("Pick a movie:", movies["title"].values)

if st.button("Recommend"):
    names, posters, trailers = recommend(selected_movie)

    cols = st.columns(5)
    for i in range(5):
        with cols[i]:
            st.image(posters[i])
            st.markdown(f"**{names[i]}**")
            if trailers[i]:
                st.markdown(
                    f"[▶ Watch Trailer]({trailers[i]})",
                    unsafe_allow_html=True,
                )
            else:
                st.markdown("🚫 Trailer Not Found")
