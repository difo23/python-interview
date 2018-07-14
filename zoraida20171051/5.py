n = int(input("Digite el numero: "))
i = 1
if n<1:
    print("Error, numero negativo")
else:
    while i <= n:
        if n % i ==0:
            print(i)
        i=i+1
