def escribirTXT(mensaje):
    try:
        with open("estado.txt","x",encoding="utf") as file:
            file.write(mensaje)
    except FileExistsError:
        with open("estado.txt","a",encoding="utf") as file:
            file.write(mensaje)