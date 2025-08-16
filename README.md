# 🎬 Movie Recommendation System

This project is a **Movie Recommendation System** built using **Machine Learning** and deployed with **Streamlit**.  
It recommends movies similar to the one selected by the user, along with posters and trailers fetched from **TMDB API**.

---

## 🚀 Features
- Recommends top similar movies based on content similarity
- Fetches movie **posters** from [The Movie Database (TMDB)](https://www.themoviedb.org/)
- Provides **YouTube trailers** for recommended movies
- User-friendly interface built with **Streamlit**
- Includes **Light / Dark Mode toggle** ✨

---

## 🛠️ Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/KumarSonu01/Machine-Learning-Projects.git
cd Machine-Learning-Projects
```
### 2. Create Virtual Environment (Optional but Recommended)
```bash
python -m venv venv
venv\Scripts\activate   # On Windows
source venv/bin/activate # On Mac/Linux
```
### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4.▶️ Running the Project

Start the Streamlit app with:
```bash
streamlit run app.py
```

Then open the link (default: http://localhost:8501) in your browser.

📂 Project Structure
.
├── app.py                     # Streamlit application
├── Movie-recommendation-system.ipynb # Jupyter Notebook (model building)
├── movie_list.pkl             # Serialized movie list
├── similarity.pkl             # Similarity matrix (may not be included due to size)
├── tmdb_5000_movies.csv       # Dataset
├── tmdb_5000_credits.csv      # Dataset
├── requirements.txt           # Python dependencies
└── README.md                  # Project documentation

⚠️ Note on Large Files

The file similarity.pkl is large (>100MB), so it may not be included in this repository.

You can generate it by running the Jupyter Notebook or download it from [Google Drive (provide link here)].

📸 Screenshots

<img width="1911" height="994" alt="Screenshot 2025-08-15 165321" src="https://github.com/user-attachments/assets/64519673-40a1-4a23-a17a-01e76a6c4a33" />
<img width="1919" height="1030" alt="Screenshot 2025-08-15 165338" src="https://github.com/user-attachments/assets/cbbaf421-0db5-4897-82e6-172f222fa40b" />


💡 Future Improvements

Add collaborative filtering

Add trailers links from youtube to be added in the recommended posters ✔️✔️✔️✔️

Enhance UI/UX ✔️
