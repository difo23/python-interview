def maxVal(n,m):
    maxv=0
    if n<m:
        maxv=m-1
    else:
        maxv=n-1
    return maxv

n1 = int(input("Digite el primer numero pls: "))
n2 = int(input("Digite el segundo numero pls: "))

m = maxVal(n1,n2)
print("El valor maximo comprendido entre ambos numeros es igual a: "+ str(m))