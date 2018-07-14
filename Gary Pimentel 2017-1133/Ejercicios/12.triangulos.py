def tipoTriang(a, b, c):
    if b == c and a == b and a == c:
        print("El triangulo es equilatero")
    elif b == c or a == c or a == b:
        print("El triangulo es isosceles")
    else:
        print("El triangulo es escaleno")


tipoTriang(3,4,5)
