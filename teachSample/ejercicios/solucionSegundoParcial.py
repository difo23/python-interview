def funcionUno(a, b): 
    return a(a(b))

def funcionDos(valor):
    resp = 0
    while(valor > 0):
        resp = valor+2
        valor-=1
    return resp

operando = funcionDos

print(funcionUno(operando,100))

#resp 3 siempre no importa que valor envies

def recorrerParametrosArbitrarios(familia, *arbitrarios, **kwords): 
    print("El parametro familia imprime: ")
    print( familia)

    print("El parametro arbitrarios imprime: ")
    for argumento in arbitrarios: 
        print( argumento) 

    print("El parametro kwords imprime: ")
    for clave in kwords: 
        print ("El valor de", clave, "es", kwords[clave])
 
recorrerParametrosArbitrarios((0,"100"), {'al':'go'}, 'rit', "mo", b="uno", a="m")

# El parametro familia imprime:
# (0, '100')
# El parametro arbitrarios imprime:
# {'al': 'go'}
# rit
# mo
# El parametro kwords imprime:
# El valor de b es uno
# El valor de a es m

def sumar(numbers):
    result = 0
    for number in numbers:
        if not number % 3 == 0:
            result += number
    print(result)

sumar([1,1,2,3,5,8,13,21,34])

# 64

f = lambda x, y=2, z=3: (x+y) * z
print(f(5, 6))

# 33

def fib(elemento):
    if elemento == 0:
        return 0
    elif elemento == 1:
        return 1
    else:
        return fib(elemento-1) + fib(elemento-2)


print(fib(6))

# 8
# O(log n) es mas eficiente porque la cantidad de pasos del algoritmo crece logaritmicamente en funcion a los datos

def printBinario(n):
    if n == 0:
        return 0
    else:
        return str(printBinario(n//2))+str(n%2)


print(printBinario(11))


# 01011

def invStr(oldStr):
    newStr = ""
    if oldStr == "":
        return oldStr
    else:
        return invStr(oldStr[1:])+oldStr[0]

def isPrimo(longitudStr, mod):
    if longitudStr % mod == 0 and longitudStr != 2:
        return False
    elif mod > longitudStr / 2:
        return True
    else:
        return isPrimo(longitudStr, mod+1)


def printInvStr(str):
    if isPrimo(len(str),2):
        return invStr(str)
    else:
        return str

print(printInvStr("abracadabra"))
print(printInvStr("para"))

# arbadacarba
# para


def bubbleSort(seq):
    if seq.__len__() <= 1: 
        return seq
    
    seqSize = seq.__len__()
    aux = 0
    for i in range(1,seqSize):
        for j in range(0, seqSize-i):
            if seq[j] > seq[j+1]:
                aux = seq[j]
                seq[j] = seq[j+1]
                seq[j+1] = aux     
    return seq

list = [4, 17 , 8 , 78, 45, 2, 4, 6, 10, 87, 1, 789, 45, 100, 54]
print(bubbleSort(list))