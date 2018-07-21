def sumaNumeros(numero):
    if numero == 1:
        return 1
    elif numero > 1:
        return (numero + sumaNumeros(numero = numero - 1))

numeroSuma = int(input("Escriba un numero para sumar los que estan entre 0 y "))
print(sumaNumeros(numeroSuma))
