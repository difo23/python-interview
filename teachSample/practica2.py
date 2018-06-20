'''
    Ejercicio 1 Escriba un programa que pida dos numeros enteros.
    El programa pedira de nuevo el segundo numero mientras no sea 
    mayor que el primero. El programa terminara escribiendo los dos.
'''

n1 = int(input("Escribe un numero:"))
n2 = int(input("Escrinbe un numero mayor que %d:" %n1))

while(n2 <= n1):
    n2 = int(input("Escrinbe otra vez un numero mayor que %d:" %n1))

print("Los numeros que has escrito son %d y %d" %(n1, n2))


'''
    Escriba un programa que pregunte cuantos numeros se van a introducir,
    pida esos numeros, y diga al final cuantos han sido pares y cuantos impares.
'''
print("Contador de Pares e Impares")
n = int(input("¿Cuantos valores va a introducir:?"))
if n < 0:
    print("Imposible!!!")
    exit()
impar = 0
par = 0
numeros = []
for valor in range (0, n):
    numero = int(input("Introduce el numero %d:" %(valor+1)))
    numeros.append(numero)
    if not(numeros[valor] % 2):
        par+=1
    else:
        impar+=1

print("Ha escrito %d numeros pares y %d numeros impares" %(par, impar))