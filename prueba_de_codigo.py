
import mysql.connector
import bcrypt #libreria de encriptacion
import streamlit as st
from datetime import datetime  # dates en python
from import_db import data, tables
from queries.queries import query_insert, query_val_user


# iniciamos la coneccion a la base de datos
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Naujac00+",
    database="semillero",
    port=3306
)


table_name = tables["tb_customers"]


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
        SELECT password_customer
        FROM {table_name}
        WHERE cc_customer = {cc_customer}
    """.format(table_name=table_name, cc_customer=cc_customer)
    cursor= connection.cursor(dictionary=True)
    cursor.execute(query)
    resultado=cursor.fetchone()
    pass_db = resultado["password_customer"]
    flag_equal_pass = bcrypt.checkpw(password_customer.encode('utf-8'), pass_db)
    
    return flag_equal_pass


def login():
    """
    Sección de inicio de sesión.
    """
    st.subheader("Login Section")
    cc_customer = st.sidebar.text_input("CC")
    password_customer = st.sidebar.text_input("Password", type="password")  
    
    if st.sidebar.button("Login"):
        flag_login = val_login(cc_customer, password_customer)
        if flag_login:
            st.success('Inicio de sesión exitoso')
            task = st.selectbox("Actividad", options=["Agregar Tareas", "Eliminar Tareas"])
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
    st.title("Simple login")
    menu = ["Home", "Login", "SignUp"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Home":
        st.subheader("Home")
    elif choice == "Login":
        login()
    elif choice == "SignUp":
        signup()

if __name__ == "__main__":
    main()



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
    """



