

import pandas as pd
import streamlit as st
import plotly.express as px
import requests
from streamlit_lottie import st_lottie
from PIL import Image
import mysql.connector
import bcrypt #libreria de encriptacion
from datetime import datetime  # dates en python
from import_db import data, tables
from queries.queries import query_insert, query_val_user

st.set_page_config(page_title="Musica") #este es el nombre que damos a la pagina web

# iniciamos la coneccion a la base de datos
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Naujac00+",
    database="semillero",
    port=3306
)

table_name = tables["tb_customers"]


# funcion para nuestra animacion
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_coding = load_lottieurl("https://lottie.host/81f93f31-9ca4-4feb-9443-3534fdd8c916/K0xDL9dHPs.json")
imagen_logo = Image.open("recursos/Captura.png")

def val_user_exist(cc_customer):
    """
    Valida si un usuario existe en la base de datos.

    Args:
        id_customer (int): ID del cliente a validar.

    Returns:
        bool: True si el usuario existe, False si no existe.
    """
    query = query_val_user.format(table_name=table_name, cc_customer=cc_customer)
    cursor = connection.cursor(dictionary=True)
    cursor.execute(query)
    resultado = cursor.fetchone()
    if resultado is None:
        return False  # Indica que no existe el id del usuario en la base de datos
    return True  # Indica que existe el usuario en la base de datos


def insert_user(cc_customer, name_customer, lastname_customer, email_customer, password_customer, register_date):
    """
    Inserta un nuevo usuario en la base de datos.

    Args:
        cc_customer (int): CC del cliente.
        name_customer (str): Nombre del cliente.
        lastname_customer (str): Apellido del cliente.
        email_customer (str): Correo electrónico del cliente.
        password_customer (str): Contraseña del cliente.
        register_date (datetime): Fecha de registro del cliente.
    """
    query = query_insert.format(
        table_name=table_name, cc_customer=cc_customer, name_customer=name_customer,
        lastname_customer=lastname_customer, email_customer=email_customer, password_customer=password_customer,
        register_date=register_date
    )
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()

name = ""
def val_login(cc_customer, password_customer):
    """
    Valida el inicio de sesión de un usuario.

    Args:
        cc_customer (int): CC del cliente.
        password_customer (str): Contraseña del cliente.

    Returns:
        bool: True si el inicio de sesión es exitoso, False si no es exitoso.
    """
    query="""
        SELECT password_customer, name_customer
        FROM {table_name}
        WHERE cc_customer = {cc_customer}
    """.format(table_name=table_name, cc_customer=cc_customer)
    cursor= connection.cursor(dictionary=True)
    cursor.execute(query)
    resultado=cursor.fetchone()
    pass_db = resultado["password_customer"]
    name = resultado["name_customer"]
    flag_equal_pass = bcrypt.checkpw(password_customer.encode('utf-8'), pass_db)
    
    return flag_equal_pass

def home():
    with st.container():
        text_column1, image_column, text_column2 = st.columns(3)
   
    with image_column:
        st.image(imagen_logo)

    with st.container():
        st.markdown("<h1 style='text-align: center; color: #49337D;'>BIENVENIDO(A) AQUI TU PIDES LA MUSICA </h1>", unsafe_allow_html=True)
        st.markdown("<h1 style='text-align: center; color: purple;'>pero antes, inicia sesión</h1>", unsafe_allow_html=True)
    
def inicio():
    with st.container():
        text_column1, image_column, text_column2 = st.columns(3)
   
    with image_column:
        st.image(imagen_logo)

    with st.container():
        st.markdown("<h1 style='text-align: center; color: #49337D;'>BIENVENIDO(A) AQUI TU PIDES LA MUSICA </h1>", unsafe_allow_html=True)
        st.markdown("<h2 style='text-align: center; color: purple;'>aqui encontraras toda la informacion acerca de futuros eventos y nuestras redes sociales</h2>", unsafe_allow_html=True)
        #st.markdown("<a title="whatsapp" href="<http://www.whatsapp.com>"><img src="recursos/whatsapp.png" alt="Whatsapp" /></a>", unsafe_allow_html=True)
        
    with st.container():
        st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("PROXIMOS EVENTOS")
        st.write(
            """PROXIMAMENTE SOLO EN CINES
            """
        )
        st.markdown("[![Foo](https://upload.wikimedia.org/wikipedia/commons/thumb/6/6b/WhatsApp.svg/150px-WhatsApp.svg.png)](http://youtube.com/naujacgamer/)")
        st.write("[youtube >>](http://youtube.com/naujacgamer)")
    with right_column:
        st_lottie(lottie_coding,height=300, key="music")


def login():
    """
    Sección de inicio de sesión.
    """
    with st.container():
        text_column1, image_column, text_column2 = st.columns(3)
   
    with image_column:
        st.image(imagen_logo)

    with st.container():
        st.markdown("<h1 style='text-align: center; color: #49337D;'>BIENVENIDO(A) AQUI TU PIDES LA MUSICA </h1>", unsafe_allow_html=True)
        st.markdown("<h1 style='text-align: center; color: purple;'>pero antes, inicia sesión</h1>", unsafe_allow_html=True)
    

    cc_customer = st.sidebar.text_input("CC")
    password_customer = st.sidebar.text_input("Password", type="password")  
    
    if st.sidebar.button("Login"):
        flag_login = val_login(cc_customer, password_customer)
        nombre = name
        if flag_login:
            st.success("BIENVENIDO")

            task = st.selectbox("Actividad", options=["Agregar Tareas", "Eliminar Tareas"])
             
            inicio()
        else:
            st.warning('Usuario/Contraseña incorrectos')

def signup():
    """
    Sección de registro de nuevos usuarios.
    """
    st.subheader("Create Account")
    cc_customer = st.sidebar.text_input("Numero identificacion")
    name_customer = st.sidebar.text_input("Nombres")
    lastname_customer = st.sidebar.text_input("Apellidos")
    email_customer = st.sidebar.text_input("Email")
    Password= st.sidebar.text_input("Contrasena", type="password")
    register_date = datetime.now()

    if st.sidebar.button("Create"):
        longitud_minima = 8
        debe_tener_mayuscula = False
        debe_tener_minuscula = False
        debe_tener_numero = False
        flag_exists = val_user_exist(cc_customer)

        if flag_exists:
            st.info("Usuario ya registrado")
        else: 
            if len(Password)>= longitud_minima:
            
                # Verificar otros requisitos
                for caracter in Password:
                    if caracter.isupper():
                        debe_tener_mayuscula = True
                    elif caracter.islower():
                        debe_tener_minuscula = True
                    elif caracter.isdigit():
                        debe_tener_numero = True
        if (debe_tener_mayuscula and debe_tener_minuscula and debe_tener_numero):
            salt = bcrypt.gensalt()

            # Hash de la contraseña con el salt
            hashed_password = bcrypt.hashpw(Password.encode('utf-8'), salt)
            hashed_password = hashed_password.decode('utf-8')
            insert_user(cc_customer, name_customer, lastname_customer, email_customer, hashed_password, register_date)
            st.success("Welcome {}".format(name_customer))
        else:
            debe_tener_mayuscula = False
            debe_tener_minuscula = False
            debe_tener_numero = False
            st.warning('error contraseña no valida')


def main():
    """Funcion principal que define la interfaz y maneja la navegacion.
    """
    menu = ["Home", "Login", "SignUp", "inicio"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Home":
        home()
    elif choice == "Login":
        login()
    elif choice == "SignUp":
        signup()
    elif choice == "inicio":
        inicio()



if __name__ == "__main__":
    main()
 
   

