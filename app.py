import streamlit as st
st.snow()
st.title(":red[Hello Welcome to My App] :sunglasses:")
st.balloons()
from PIL import Image
image=Image.open('intern.jpg')
st.image(image,caption='My First App')
if(st.button("Click Here...")==True):
    st.subheader("Have a Nice Day!")