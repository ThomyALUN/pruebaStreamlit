import pandas as pd
import streamlit as st

def escribirDatos(nombre, correo, edad, carrera, matriculas):
    exitoso=True
    mensaje=f"{nombre},{correo},{edad},{carrera},{matriculas}\n"
    try:
        with open("estado.csv","x",encoding="utf") as file:
            file.write("Nombre,Correo,Edad,Carrera,Matriculas\n")
            file.write(mensaje)
    except FileExistsError:
        exitoso=revisarRepeticionCorreo(correo)
        if exitoso:
            with open("estado.csv","a",encoding="utf") as file:
                file.write(mensaje)
    return exitoso

def revisarRepeticionCorreo(correo):
    sePuedeIngresar=True
    df=pd.read_csv("estado.csv")
    if any(df["Correo"]==correo):
        st.warning(f"El correo {correo} ya esta registrado",icon="⚠️")
        sePuedeIngresar=False
    return sePuedeIngresar