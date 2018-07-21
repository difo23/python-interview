def repeticiones(cantidad):
    if cantidad == 0:
        return "End"

    else:
        print("Jorvy")
        repeticiones(cantidad = cantidad - 1)

repeticiones(int(input("Cuantas veces quiere repetir el nombre?")))