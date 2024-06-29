import numpy as np
import pandas as pd
import streamlit as st
import seaborn as sns
from pandas_profiling import profile_report
from streamlit_pandas_profiling import st_profile_report




# webapp ka title
st.markdown('''
# **Exploratory data analysis web application**
this app is developed by condanics youtube channel called **EDA APP**
  ''')

# how to uplode a file from pc
with st.sidebar. header("upload your dataset (.csv)"):
    uploaded_file = st.sidebar.file_uploader("uplodad your file", type=['csv'])
    df = sns.load_dataset('titanic')
    st.sidebar.markdown("[EXample CSV file](https://www.kaggle.com/louise2001/quantum-physics-articles-on-arxiv-1994-to-2009/download")
    
    
# profilig report for pandas
if uploaded_file is not None:
  @st.cache
  
  def load_csv():
   csv = pd.read_csv(uploaded_file) 
   return csv
   df = load_csv()
   pr = profile_report(df, explorative = True)
   st.header('** input DF**')
   st.write(df)
   st.write('---')
   st.header('**profliing report with pandas**')
   st_profile_report(pr)
else:
  st.info (' awiting for csv file,upload kar b do agar kam linna hay?')
  if st.button('prees to use example data'):
  #example dataset
     @st.cache
 
     def load_data():
       a = pd.DataFrame ( np. random.rand(100,6),
                        columns=['age','bannan','codanics','ayyan ali ','ishal', 'izal'])
       return a
     df = load_data
     

  def load_data():
   pr = profile_report(df, explorative = True)
   st.header('** input dataframe**')
   st.write(df)
   st.write('---')
   st.header('**profliing report with pandas**')
   st_profile_report(pr)