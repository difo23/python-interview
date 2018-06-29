
milista = [1, 2, 3, 4, 5, 6]
print("Gráfica a")
for i in range(6):

    print(milista)
    milista.pop()                       

milista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("Gráfica b")
for j in range(1, 10, 2):

    print(milista[0:j])             

print("Gráfica c")
for k in range(1, 10, 2):
    print(milista[0:k])
    while k == 9:
        for h in range(8, 0, -2):
            print(milista[0:h-1])
            k -= 1