def Cdig(n, d):
    contador = 0
    if n == 0:
        return contador
    elif n % 10 == d:
        return contador+1 + Cdig(n//10, d)
    else:
        return Cdig(n//10, d)

numero = int(input("Escriba un numero cualquiera (mientras mas grande y variado mejor, en base 10): "))
numeroBusq = int(input("\nIntroduzca un numero para ver cuantas veces se repite en el anterior: "))

print("\nEl numero que escribio se repite: %s veces" %(Cdig(numero, numeroBusq)))