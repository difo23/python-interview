print("Veamos que tipo de triangulo sera, dependiendo de las longitudes de sus lados:")
def tipoTriang(a, b, c):
    if a == b and b == c and a == c:
        print("Es un triangulo Equilatero\nYa que posee todos sus lados iguales.")

    elif a == b or a == c or b == c:
        print("Es un triangulo Isoceles\nYa que dos de sus lados son iguales y uno diferente.")
    else:
        print("Es un triangulo Escaleno\nYa que todos sus lados son irregulares con respecto a ellos mismos.")

tipoTriang(input("Lado A mide: "), input("Lado B mide: "), input("Lado C mide: "))
print("Fin del Programa")