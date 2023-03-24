import streamlit as st

from funciones import *

carreras=["---","Ingeniería Electrónica", "Ingeniería Eléctrica", "Administración de Sistemas Informáticos", "Ingeniería Civil"]
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

st.subheader("A continuación podrá ingresar algunos de sus datos")

carreraSelec = st.selectbox(
    '¿Qué carrera estudias?',
    carreras,
    key="carrera")

matricSelec = st.selectbox(
    '¿Cuántas matrículas llevas?',
    matriculas,
    key="matricula")

if carreraSelec==carreras[0] or matricSelec==matriculas[0]:
    datosIngresados=False
else:
    datosIngresados=True

if st.button("Enviar"):
    if datosIngresados:
        st.write("Tú estudias ", carreraSelec, " y llevas ", matricSelec, " matrículas en la universidad")
        escribirDatos(f"{carreraSelec},{matricSelec}\n")
    else:
        st.warning('Aún no has ingresado completamente tus datos', icon="ℹ️")