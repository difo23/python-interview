def repeticion(numero,nombre):
    if numero == 0:
        return nombre
    else:
        print(nombre)
        return repeticion(numero-1,nombre)

repeticion(int(input("numero ")),input("nombre"))