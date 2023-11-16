

import pandas as pd
import streamlit as st
import plotly.express as px
import requests
from streamlit_lottie import st_lottie
from PIL import Image

st.set_page_config(page_title="Musica") #este es el nombre que damos a la pagina web


# funcion para nuestra animacion
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_coding = load_lottieurl("https://lottie.host/81f93f31-9ca4-4feb-9443-3534fdd8c916/K0xDL9dHPs.json")
imagen_logo = Image.open("recursos/Captura.png")


with st.container():
    text_column1, image_column, text_column2 = st.columns(3)
   
    with image_column:
        st.image(imagen_logo)

with st.container():
    st.markdown("<h1 style='text-align: center; color: #49337D;'>BIENVENIDO(A) AQUI TU PIDES LA MUSICA </h1>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center; color: purple;'>Y SIN TANTO BLA BLA BLA INICIEMOS DESLIZA HACIA ABAJO </h1>", unsafe_allow_html=True)
    

 
   

with st.container():
    st.subheader("hola mundo")
    st.title("introduccion")
    st.write("esto es uin texto muy largo")
    st.write("[Mas Información >](http://youtube.com/naujacgamer)")

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("mi objetivo")
        st.write(
            """texto 1
            texto2
            texto 3
            mucho texto
            """
        )
        st.write("[youtube >>](http://youtube.com/naujacgamer)")
    with right_column:
        st_lottie(lottie_coding,height=300, key="music")


with st.container():
    st.write("---")
    st.header("algun texto aqui")
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(imagen_logo)
    with text_column:
        st.write(
            """
            Muchas veces, después de hacer un cálculo, 
            queremos mostrar de forma sencilla algún resultado de tal forma que cualquiera lo pueda visualizar.
            A veces, el resultado no es algo sencillo y queremos proporcionar herramientas para que otros puedan toquetear los datos y que vean actualizaciones de forma interactiva.
            """
        )
        st.markdown("[mas informacion...](https://pybonacci.org/2020/02/20/haciendo-un-dashboard-con-streamlit-en-python/)")