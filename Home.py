import requests
import streamlit as st
from fast_api_server import obtener_fecha, contador_llamadas

# APP CONFIG
st.set_page_config(page_title="Marvik - Will", page_icon="🤖")

# TITLE 
st.title('Wilber Jiménez (Will)´s Test')
st.title('Marvik`s Candidate 🤖')

#TEST 1
st.header("Test 1: Time Series")
st.link_button("Go to de Google Colab", "https://colab.research.google.com/drive/1q2A1iOXbjCaWFUSPjI07TgT7INmfKBYA#scrollTo=8gVfdvyk6xaK")

#TEST 2

st.header("Test 2: FAST API")


#TEST 3
st.header("Test 3: Style-Based Desings - Summary")
st.write("The only constant is change. Some of the NVIDIA Research team presented in 2019 how the traditional way for architechure Generative Adversarial Networks can be improved in its performance and quality through new methods")
st.write("")
