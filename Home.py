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
# URL base de la API FastAPI
base_url = "http://localhost:8000"

st.title("FastAPI + Streamlit")

# Función para realizar la llamada a la API y mostrar los resultados
def llamar_api_obtener_fecha(formateo):
    endpoint = "/obtener_fecha"
    url = base_url + endpoint
    payload = {"formateo": formateo}
    response = requests.post(url, json=payload)
    if response.status_code == 200:
        data = response.json()
        st.write("Fecha obtenida:", data["fecha_actual"])
    else:
        st.error("Error al obtener la fecha")

# Función para obtener el contador de llamadas
def obtener_contador_llamadas():
    endpoint = "/contador_llamadas"
    url = base_url + endpoint
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        st.write("Contador de llamadas:", data["contador_llamadas"])
    else:
        st.error("Error al obtener el contador de llamadas")

# Interfaz de usuario con Streamlit
option = st.selectbox(
    'Selecciona el formato de fecha:',
    ('aaaa-mm-dd hh:ii:ss', 'aaaa-dd-mm')
)

if st.button("Obtener Fecha"):
    if option == 'aaaa-mm-dd hh:ii:ss':
        llamar_api_obtener_fecha(True)
    else:
        llamar_api_obtener_fecha(False)

# Mostrar el contador de llamadas
obtener_contador_llamadas()


#TEST 3
st.header("Test 3: Style-Based Desings - Summary")
st.write("The only constant is change. Some of the NVIDIA Research team presented in 2019 how the traditional way for architechure Generative Adversarial Networks can be improved in its performance and quality through new methods")
st.write("")
