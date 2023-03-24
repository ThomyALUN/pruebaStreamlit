import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Registros: Encuesta",
    page_icon=":floppy_disk:",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# Este es mi primer proyecto. ¿No te parece muy cool? :sunglasses:"
    }
)

st.title(("Estudiantes registrados").upper())

if st.button("Ver registros"):
    try:
        datos=pd.read_csv("estado.csv")
        st.dataframe(datos)
    except FileNotFoundError:
        st.warning("Aún no se han realizado registros.")
