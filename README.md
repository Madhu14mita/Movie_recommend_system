# 🎬 Movie Recommender System Using Machine Learning

Welcome to the **Movie Recommender System** — an intelligent app that helps users discover new movies based on their preferences using machine learning techniques and content-based filtering. Built with **Streamlit**, this project delivers recommendations along with visually appealing movie posters fetched from TMDB.

🔗 **Live Demo:** [Click to try it out!](https://movierecommendsystem-mhglmxi6xmpqy69mmicvsx.streamlit.app/)

---

## 🚀 Features

- 🎯 Recommends 5 movies based on the selected movie
- 🧠 Uses **cosine similarity** on **CountVectorizer**-based feature vectors
- 🖼️ Displays movie posters using **TMDB API**
- 📱 Interactive UI built with **Streamlit**
- ☁️ Deployed for free on **Streamlit Cloud**

---

## 🛠️ Tech Stack

| Category        | Tools Used                        |
|----------------|-----------------------------------|
| Language        | Python                            |
| ML Technique    | CountVectorizer + Cosine Similarity |
| Libraries       | `pandas`, `scikit-learn`, `pickle`, `requests`, `streamlit`, `gdown` |
| Deployment      | Streamlit Cloud                   |
| Data Source     | Movie metadata + TMDB API         |

---

## 🧪 How It Works

1. **Movie metadata** is processed using **CountVectorizer** on combined features (like genres, keywords, overview, etc.).
2. A **cosine similarity matrix** is computed across all movie vectors.
3. When a user selects a movie, the system recommends the top 5 most similar movies.
4. The **TMDB API** fetches and displays movie posters dynamically.

---

## 📦 Project Structure

movie_recommend/
├── app.py # Main Streamlit application
├── requirements.txt # Python dependencies
├── README.md # Project documentation
└── movie.pkl # Movie metadata (from Google Drive)
└── similarity.pkl # Similarity matrix (from Google Drive)

---
☁️ Deployment
Hosted on Streamlit Cloud

.pkl files are loaded at runtime from Google Drive using gdown (no large files in repo)


