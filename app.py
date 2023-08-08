import streamlit as st
import pickle
import pandas as pd
import requests

st. set_page_config(layout="wide")

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[0:20]:
        # fetch the movie poster
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)
    return recommended_movie_names,recommended_movie_posters

# loaded the data from save model
# movies_dict = pickle.load(open('C:/Users/emon1/OneDrive/Desktop/ML Advanced Project/1 Movie Recommender System Project/movies_dict.pkl','rb'))
movies_dict = pickle.load(open('movies_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)

# similarity = pickle.load(open('C:/Users/emon1/OneDrive/Desktop/ML Advanced Project/1 Movie Recommender System Project/similarity.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))

# set title
st.title('Movie Recommendation System\n Made by Emon Hasan')

# select box for all movie names
# selected_movie_name = st.selectbox('how would you like to be connected?',movies['title'].values)

movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

if st.button('Show Recommendation'):
    recommended_movie_names,recommended_movie_posters = recommend(selected_movie)
    
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.image(recommended_movie_posters[0])
        st.text(recommended_movie_names[0])
    with col2:
        st.image(recommended_movie_posters[1])
        st.text(recommended_movie_names[1])
    with col3:
        st.image(recommended_movie_posters[2])
        st.text(recommended_movie_names[2])
    with col4:
        st.image(recommended_movie_posters[3])
        st.text(recommended_movie_names[3])
    with col5:
        st.image(recommended_movie_posters[4])
        st.text(recommended_movie_names[4])

    col6, col7, col8, col9, col10 = st.columns(5)
    with col6:
        st.image(recommended_movie_posters[5])
        st.text(recommended_movie_names[5])
    with col7:
        st.image(recommended_movie_posters[6])
        st.text(recommended_movie_names[6])
    with col8:
        st.image(recommended_movie_posters[7])
        st.text(recommended_movie_names[7])
    with col9:
        st.image(recommended_movie_posters[8])
        st.text(recommended_movie_names[8])
    with col10:
        st.image(recommended_movie_posters[9])
        st.text(recommended_movie_names[9])
        
    col11, col12, col13, col14, col15 = st.columns(5)
    with col11:
        st.image(recommended_movie_posters[10])
        st.text(recommended_movie_names[10])
    with col12:
        st.image(recommended_movie_posters[11])
        st.text(recommended_movie_names[11])
    with col13:
        st.image(recommended_movie_posters[12])
        st.text(recommended_movie_names[12])
    with col14:
        st.image(recommended_movie_posters[13])
        st.text(recommended_movie_names[13])
    with col15:
        st.image(recommended_movie_posters[14])
        st.text(recommended_movie_names[14])
    
    col16, col17, col18, col19, col20 = st.columns(5)
    with col16:
        st.image(recommended_movie_posters[15])
        st.text(recommended_movie_names[15])
    with col17:
        st.image(recommended_movie_posters[16])
        st.text(recommended_movie_names[16])
    with col18:
        st.image(recommended_movie_posters[17])
        st.text(recommended_movie_names[17])
    with col19:
        st.image(recommended_movie_posters[18])
        st.text(recommended_movie_names[18])
    with col20:
        st.image(recommended_movie_posters[19])
        st.text(recommended_movie_names[19])