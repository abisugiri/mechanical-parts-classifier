import streamlit as st
from PIL import Image

def run():
    # Add Picture
    image = Image.open('mechanical_parts.jpg')
    st.image(image, caption='Mechanical Parts')
    # Title
    st.title('About This Project')
    st.markdown('---')
    st.write('###### The main objective of this project is implementing a machine learning model, namely Convolutional Neural Networks (CNN), to classify four categories of mechanical parts: bolt, locatingpin, nut, and washer')
    st.markdown('---')
    


if __name__ == '__main__':
    run()