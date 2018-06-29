def funcion (a,b):
    numero=str(a)
    numero2=str(b)
    cont= 0
    for eso in numero:
        if eso == numero2:
            cont+=1
    return (cont)

print(funcion(246588,2))

