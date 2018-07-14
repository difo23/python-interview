
# Solucion pimer examen parcial de algoritmos estructurados

'''
	1. Indica que valor imprimen estos fragmentos de codigo(20pts):
'''
num =4 # El numero maximo de repeticiones 4
res = 0
for valor in range(num): # las repeticiones van asignando a valor = 0, 1, 2 ,3 recordar que empiza en 0
	res += valor # suma res= res +valor, res= 0+0, 0+1, 1+2, 3+3; res = 6
print(res)

# Respuesta res=6

#       0  1  2  3  4  5   6
list = [1, 1, 6, 3, 5, 8, 4] # Es importante ver los indices del arreglo  
print(list[list[list[2]]]) # list[4] = devuelve el valor 5; con el valor devuelto list[5] = valor devuelto 8

#Respuesta res = 8

for i in range(10): # La variable i cambiara de valor 0,1,2,3,4,5,6,7,8,9
    if not i % 2 == 0: # la condicion i%2==0 sera true para los numeros pares, not negara esto haciendo que el el if vea un false cuando esto ocurra, es decir solo sera verdad para los numeros impares.
   		print(i+1)# imprimira el valor de i cada vez que sea impar sumandoles 1; 1+1= 2, 3+1= 4, 5+1=6, 7+1 = 8 y 9+1 = 10

print((8**2) and (0) or (40//5))
# evaluamos de izquierda a derecha
# 8**2 = 64 > es true
# 0 es false
# x and y; 64 and 0; Retorna x si x es False; y en caso contrario. en este  caso retorna y que en este caso es 0
#40//5 = 8 > 0 es true
#x or y; 0 or 8;	Retorna y si x es False; x en caso contrario. En este caso retorna  y=8 porque x es falso.

# respuesta 8

'''
	2.Haga un programa al cual se le digite una cantidad expresada en pesos (Menudo ) e imprima la misma cantidad expresada  en billetes de 1, 5,  20, 50  y 100. (30pts).
'''

def cantidad(pesos):
    cientos = 0 # una yarda tiene 36 pulgadas
    cincuenta = 0 # un pie tiene 12 pulgadas
    veinte= 0
    cinco= 0
    print("Introduciste %d pesos y te devolvemos:" %pesos)
    while pesos >= 100:
        cientos  += 1
        pesos -= 100

    while pesos >= 50:
        cincuenta  += 1
        pesos -= 50

    while pesos >= 20:
        veinte += 1
        pesos -= 20

    while pesos >= 5:
        cinco += 1
        pesos -= 5
    
    print(" %d Billetes de 100, %d billetes de 50, %d billetes de 20, %d billetes de 5 y %d pesos " %(cientos, cincuenta, veinte, cinco, pesos))

cantidad(13577)

''' 3.Escriba un programa que pregunte cuántos números se van a introducir, pida esos números, y diga al final cuantos han sido primos.
'''

cantidadNumeros = int(input("Digita la cantidad de numeros que vas a introducir:"))
esPrimo = True
contadorPrimos = 0

for valor in range(cantidadNumeros):
    numero = int(input("Introduce el numero %d a evaluar" %(valor+1)))
    for num in range(2,numero): 
        if numero % num == 0:# si el numero divisible por cualquier valor entre 2 y numero resulta no ser primo
            esPrimo = False
            break
        else:
            esPrimo = True
    if esPrimo:
        contadorPrimos += 1

print("La cantidad de numeros primos introducidos es: %d" %contadorPrimos)       
    
'''    
4) Hacer una función cdig(n), se desea que dicha función retorna la cantidad de dígitos pares e impares que hay en el número n. Por ejemplo: cdig(1241), El número 1241 tiene 2 dígitos pares y 2 dígitos impares.(20 pts)'''


def cdig(n):
    numeroStr = str(n)
    contadorPares = 0 
    contadorImpares = 0 6234 6 2 3 4
    for numerochar in numeroStr:
        print(numerochar)
        numero = int(numerochar)
        if numero % 2 == 0:
            contadorPares += 1
        else:
            contadorImpares +=1
    print("Numeros pares introducidos: %d, numeros impares: %d" %(contadorPares, contadorImpares))
            
            

cdig(1241)


















