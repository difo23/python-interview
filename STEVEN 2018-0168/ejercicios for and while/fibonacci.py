meses = int(input("cuantos meses pasaran: "))
num = 1
num1 = 0
num2 = 0
for i in range(0,meses-1):
    num2 = num1
    num1 = num
    num = num1 + num2
    print(num)    