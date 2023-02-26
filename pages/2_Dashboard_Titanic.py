import streamlit as st
import matplotlib.pyplot as plt
from matplotlib import image
import pandas as pd
import plotly.express as px
import os
import joblib

#absolute path tho this file
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
#absolute path to this file's root directory
PARENT_DIR = os.path.join(FILE_DIR,os.pardir)
#absolute path of directory_of_interest
dir_of_interest=os.path.join(PARENT_DIR,"resources")
IMAGE_PATH=os.path.join(dir_of_interest,"images","titanic.jpg")
DATA_PATH = os.path.join(dir_of_interest,"data","titanic.csv")
st.title("Dashboard-Titanic Data")
img=image.imread(IMAGE_PATH)
st.image(img)
df=pd.read_csv(DATA_PATH)
st.snow()
st.subheader("Dataframe of Titanic DataSet")
st.dataframe(df)

st.subheader('Survival Rate')
survival_count = df['Survived'].value_counts()
st.text(f'Survival rate = {survival_count.values[1]/sum(survival_count):.2%}')

# simple plotting
fig, ax = plt.subplots(1, 2, figsize=(15, 5))
survival_count.plot.bar(ax=ax[0])
df['Age'].plot.hist(ax=ax[1])
st.pyplot(fig)
