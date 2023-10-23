import streamlit as st
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')
st.title("Data Analysis")
col1, col2, col3 = st.columns(3)
col1.metric("Year", '$3652', '$3501')
col2.metric('India', '$4201')
#mining data

#st.sidebar.button('hello')


#df1 = df.drop(['ID','Year','Category', 'Product','UnitPrice', 'TotalPrice'], axis='columns')
#st.write(df1)
#st.map(df1)

#if st.button('load dataset'):
#if st.sidebar.button('hello')

if st.sidebar.button('load description'):
    st.write(df.describe())

#a1 = pd.DataFrame(df['Year'], df['TotalPrice'])
#st.line_chart(df['Year'], df['TotalPrice'])
if st.sidebar.button('load bar chart'):
    df2= df.head(20)
    fig = plt.figure(figsize=(10,8))
    plt.bar(df2['Product'], df2['Qty'])
    st.pyplot(fig)

