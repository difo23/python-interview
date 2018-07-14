
listadenumeros = [1, 2, 3, 4, 5, 6]
print("Gráfica a") 
for i in range(6):

    print(listadenumeros)
    listadenumeros.pop()                       

listadenumeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("Gráfica b") 
for a in range(1, 10, 2):

    print(listadenumeros[0:a])              

print("Gráfica c")
for p in range(1, 10, 2):
    print(listadenumeros[0:p])
    while p == 9:
        for h in range(8, 0, -2):
            print(listadenumeros[0:h-1])
            p -= 1




