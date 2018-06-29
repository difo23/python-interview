def maxVal(a,b):
    if a > b:
        return(a,"es el mayor")
    elif a == b:
        return("son el mismo valor")
    else:
        return(b,"es el mayor")    
a = int(input("primer numero: "))
b = int(input("segundo numero: "))
print(maxVal(a,b))        