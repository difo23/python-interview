
milista = [1, 2, 3, 4, 5, 6]
print("Gráfica a")
for i in range(6):

    print(milista)
    milista.pop()                       # eliminar el ultimo elemento de la lista

milista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("Gráfica b")
for j in range(1, 10, 2):

    print(milista[0:j])              # me imprime el elemento del 0 a j de la lista

print("Gráfica c")
for k in range(1, 10, 2):
    print(milista[0:k])
    while k == 9:
        for h in range(8, 0, -2):
            print(milista[0:h-1])
            k -= 1




