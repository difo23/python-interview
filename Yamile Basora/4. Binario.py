def printBinario(n):
    if n==0:
        return 0
    else:
        return str(printBinario(n//2))+str(n%2)