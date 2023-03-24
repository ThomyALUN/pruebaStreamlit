import streamlit as st

from funciones import *

carreras=["---", "Administración de Empresas", "Administración de Sistemas Informáticos", "Arquitectura",
            "Ciencias de la Computación", "Gestión Cultural", "Ingeniería Civil", "Ingeniería Eléctrica",
            "Ingeniería Electrónica", "Ingeniería Física", "Ingeniería Industrial", "Ingeniería Química",
            "Matemáticas"
            ]
matriculas=["---"]+[str(i+1) for i in range(10)]


st.set_page_config(
    page_title="Encuesta UNAL",
    page_icon=":school:",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# Este es mi primer proyecto. ¿No te parece muy cool? :sunglasses:"
    }
)


st.title("Formulario")

st.subheader("A continuación podrás ingresar algunos de tus datos")

nombre=st.text_input(label="Nombre",placeholder="Juanito Peréz")

edad=st.number_input(label="Edad", format="%d", min_value=0)

correo=st.text_input(label="Correo",placeholder="juanitoperez@unal.edu.co")

correoValido=False
if correo: 
    if not correo.islower():
        st.warning("El correo institucional no contiene carácteres mayúsculos",icon="⚠️")
    elif correo[-12:]!="@unal.edu.co":
        st.warning(f"El correo institucional debe terminar con @unal.edu.co")
    else:
        correoValido=True

carreraSelec = st.selectbox(
    '¿Qué carrera estudias?',
    carreras,
    key="carrera")

matricSelec = st.selectbox(
    '¿Cuántas matrículas llevas?',
    matriculas,
    key="matricula")

# any() funciona como un OR múltiple
if any([ not nombre, not correoValido, not edad, carreraSelec==carreras[0], matricSelec==matriculas[0] ]):
    datosIngresados=False
else:
    datosIngresados=True

if st.button("Enviar"):
    if datosIngresados:
        st.write("Tú estudias ", carreraSelec, " y llevas ", matricSelec, " matrículas en la universidad")
        escribirDatos(nombre, correo, edad, carreraSelec, matricSelec)
    else:
        st.warning('Aún no has ingresado completamente tus datos', icon="ℹ️")