
def tipoTriangulo(a, b, c):
    if a == b and b == c and a == c:
        print("El triangulo es Equilatero \nEs un polígono regular con tres lados iguales.  ")

    elif a == b or a == c or b == c:
        print("El triangulo es isósceles \nEs un polígono de tres lados, siendo dos iguales y uno desigual.")
    else:
        print("El triangulo es escaleno \nEs un polígono de tres lados, siendo todos éstos diferentes.")


tipoTriangulo(2, 2, 6)
tipoTriangulo(848, 848, 848)
tipoTriangulo(795587, 154554, 166744)