# import labraris
import streamlit as st
import plotly.express as px
import pandas as pd


# import dataset
st.title("plotly or streamlit ko mala kar app banna")
df = px.data.gapminder()
st.write(df)
#st.write (df.head())
st.write(df.columns)
# summary stat
st.write(df.describe())



# data managment
year_option = df['year'].unique().tolist()
year = st.selectbox ("which year should we plot?", year_option,0)
# df = df[df['year']==year]


 # plotting
fig = px.scatter(df ,x='gdpPercap' ,y = 'lifeExp', size = 'pop',color='continent', hover_name= 'continent',
                log_x=True ,size_max=55 ,range_x=[100,100000], range_y=[20,90],
                animation_frame='year', animation_group='country')



fig.update_layout(width=1000 , height = 400)
st.write(fig) 