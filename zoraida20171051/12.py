def tripoTriangulo(a,b,c):
    if(a==b and a==c):
        return 1
    if(a==b or b==c or a==c):
        return 2
    return 3

a= float(input("Digite el primer numero: "))
b= float(input("Digite el segundo numero: "))
c= float(input("Digite el tercer numero: "))
 
print(tripoTriangulo(a,b,c))