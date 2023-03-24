def escribirDatos(mensaje):
    try:
        with open("estado.csv","x",encoding="utf") as file:
            file.write(mensaje)
    except FileExistsError:
        with open("estado.csv","a",encoding="utf") as file:
            file.write(mensaje)