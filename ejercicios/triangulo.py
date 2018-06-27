print(" Quieres saber que tipo de  triangulo tienes :) ")
a = int(input("primera medida: "))
b = int(input("segunda medida: "))
c = int(input("tercera medida: "))
def tipTriangulo(a,b,c):
    if a != b and b != c and a != c:
        print("Es escaleno") 
    elif a == b and a == c and c == b:
        print("Es equilatero")
    else:
        print("Es isosceles")
print(tipTriangulo(a,b,c))   