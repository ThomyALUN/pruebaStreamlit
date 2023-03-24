def escribirDatos(nombre, correo, edad, carrera, matriculas):
    mensaje=f"{nombre},{correo},{edad},{carrera},{matriculas}\n"
    try:
        with open("estado.csv","x",encoding="utf") as file:
            file.write("Nombre,Correo,Edad,Carrera,Matriculas\n")
            file.write(mensaje)
    except FileExistsError:
        with open("estado.csv","a",encoding="utf") as file:
            file.write(mensaje)