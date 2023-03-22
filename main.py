import streamlit as st

st.set_page_config(page_title="Brahian es gay")

st.title("Formulario")

carreras=[" ","Electrónica", "Eléctrica", "ASI", "Civil"]
matriculas=[""]+[str(i+1) for i in range(10)]

carreraSelec = st.selectbox(
    '¿Qué carrera estudias?',carreras,key="carrera")

matricSelec = st.selectbox(
    '¿Cuántas matrículas llevas?',
    matriculas,
    key="matricula")


if carreraSelec==carreras[0] or matricSelec==matriculas[0]:
    datosIngresados=False
else:
    datosIngresados=True

if datosIngresados:
    if matricSelec=="1":
        "Tú estudias ", carreraSelec, " y llevas ", matricSelec, " matrícula en la universidad"
    else:
        "Tú estudias ", carreraSelec, " y llevas ", matricSelec, " matrículas en la universidad"