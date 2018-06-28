num=int(input('Ingrese un numero:'))
If num>=0:
    acu = 0
    for i in range (1,num+1):
       if num%i!=0:
           acu=acu
    else:
         Print(i)
else: 
       Print('El número introducido no es valido')