num=int(input('ingrese un numero:'))
If num>=0:
    acu = 0
    for i in range (1,num+1):
       if num%i!=0:
           acu=acu
    else:
         Print(i)
else: 
       Print('el número introducido no es valido')