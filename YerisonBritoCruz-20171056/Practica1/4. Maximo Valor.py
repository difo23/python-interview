num = int(input("Introduce el valor n "))
num2 = int(input("Introduce el valor m "))


def maxVal(n, m):

    if n > m:
        print(" El mayor valor es n %d " % n)
    else:
        print(" El mayor valor es m %d " % m)


maxVal(num, num2)
