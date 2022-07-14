import streamlit as st

from sqlalchemy import create_engine
import pandas as pd
import pymysql

import plotly.graph_objects as go
import plotly.express as px

##########
# data
##########
engine = create_engine("mysql+pymysql://data-student:u9AB6hWGsNkNcRDm@data.engeto.com:3306/data_academy_04_2022")
df_bikes = pd.read_sql(sql='select * from edinburgh_bikes limit 20000', con=engine)

##########
# vizualizace
##########

st.title('Moje prvni appka')

st.write('Toto je moje prvni aplikace, kterou udelam. Dalsi radky budou super COOL!')

page = st.sidebar.radio('Select page', ['Mapa', 'Thomson'])

if page == 'Mapa':
    st.write('Moapa pouzivani sdilenych kol v Edinburgu')
    fig = px.scatter_mapbox(df_temp,lat='start_station_latitude', lon='start_station_longitude')
    fig.update_layout(mapbox_style="open-street-map")
    fig.show()

if page == 'Thomson':
    st.write('Tomson sampling')
