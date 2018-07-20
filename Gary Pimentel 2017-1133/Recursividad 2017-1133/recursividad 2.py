def gaus (n):
    if n == 1:
        return 1
    else:
        return n + gaus(n - 1)

print(gaus(int(input("numero: ")))) 
#n*(n + 1)/2