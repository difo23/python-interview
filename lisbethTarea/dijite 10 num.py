y=0
z=0
c=0
d=0
mx=0
mini=999999
contadorm:0
contadorM:0
for i in range(10):
     x=int(input('dijite su numero '))
     y=y+x
     z=y+z/1       
     c=y/10

     if mx<=x:
        d=x
        mx=d
    
        
       

     if x<mini:
          d=x
          mini=d
          

     
     
     


print('suma de dichos valores: ',y, 'suma de los cuadrados: ',z,'el promedio es: ',c,'el minimo es: ',mini,'el maximo es: ',mx)
