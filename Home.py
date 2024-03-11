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
st.header("Test 3: Style-Based Desings")
st.subheader("Summary in my terms")
st.write("The only constant is change. Some of the NVIDIA Research team presented in 2019 how the traditional way for architechure Generative Adversarial Networks can be improved in its performance and quality through two new automated methods that are applicable to any generator architecture.")
st.write("The computer vision capabilitties for detect humans and their movements have been rised with the Style Based Desing. For testing, real time implementation and future discoveries the NVIDIA team has share HumanFaces Dataset with the mayor variaty and quality for empower the next generation of computer vision solutions. The future starts now.")
st.subheader("Summary empowered with ChatGPT and human final touch:")
st.write("The only constant is change. In 2019, some members of the NVIDIA Research team presented how the traditional architecture for Generative Adversarial Networks can be enhanced in performance and quality through two new automated methods applicable to any generator architecture")
st.write("The capabilities of computer vision to detect humans and their movements have been elevated with the Style-Based Design. For testing, real-time implementation, and future discoveries, the NVIDIA team has shared the HumanFaces Dataset, offering a diverse and high-quality collection to empower the next generation of computer vision solutions. The future begins now.")
