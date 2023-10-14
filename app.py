import streamlit as st
import pickle
import pandas as pd

st.title('Movie Recommender System')

movies_dict=pickle.load(open('movies_dict.pkl' , 'rb'))
movies=pd.DataFrame(movies_dict)

similarity=pickle.load(open('similarity.pkl','rb'))


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies=[]

    for i in movies_list:
        movies_id=i[0]

        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies

st.title('movie recommender system')

selected_movie_name=st.selectbox(
    'Search any movie',
    movies['title'].values)

if st.button('Recommend'):
    recommendations=recommend(selected_movie_name)
    for i in recommendations:
        st.write(i)

