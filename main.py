import streamlit as st
import pickle
import pandas as pd

st.title("Movie Recommender System")

movies_dict=pickle.load(open('df_dict.pkl','rb'))
movies=pd.DataFrame(movies_dict)

all_similarities=pickle.load(open('all_similarities.pkl','rb'))
selected_movie = st.selectbox(
    'Please select the movie',
    movies['title'].values, placeholder="Please select the movie")


def recommend(movie):
    movie_index=movies[movies['title']==movie].index[0]
    distances=all_similarities[movie_index]
    movies_list=sorted(list(enumerate(distances)),reverse=True,key=lambda c:c[1])[1:6]
    print('\nRecommended movies based on the input movie you entered:\n')
    recommendations=[]
    for i in movies_list:
        recommendations.append(movies.iloc[i[0]].title)
    return recommendations

if st.button('Recommend'):
    st.subheader('Recommendations are:')
    all_recommendations=recommend(selected_movie)
    for i in all_recommendations:
        st.write(i)



