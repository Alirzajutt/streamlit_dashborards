# import streamlit as st
# import pandas as pd
# from sklearn.ensemble import RandomForestClassifier
import streamlit as st
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier


st. wirte("""
# Random Forestsd classifier app
## made by ali raza
this app predict the type of iris based on sepal length ,sepal width, petal length, and petal width.
""")

st.sidebar.header(' user input parameters')