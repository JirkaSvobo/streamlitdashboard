import streamlit as st


st.title('Moje prvni appka')

st.write('Toto je moje prvni aplikace, kterou udelam. Dalsi radky budou super COOL!')

page = st.sidebar.radio('Select page', ['Test', 'Tomson'])

if page == 'Test':
    st.write('Toto je moje prvni aplikace, kterou udelam. Dalsi radky budou super COOL!')

if page == 'Tomson':
    st.write('Tomson sampling')
