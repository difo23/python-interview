num = int(input("Introduce el valor de n: "))
num2 = int(input("Introduce el valor de m: "))


def maxVal(n, m):

    if n > m:
        print(" El mayor valor es n %d " % n)
    else:
        print(" El mayor valor es m %d " % m)


maxVal(num, num2)
