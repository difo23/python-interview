Suma=0
Cuadrado=0
Promedio=0
Maximo=0
Mínimo=1000000000000

For i in range(10):
     num=int(input('ingrese un numero:'))
     Suma= suma+num
      
      if num>=maximo:
             máximo=num
      Elif num<=minimo:
                 minimo=num

Promedio = suma/10
Cuadrado = suma**2
Print()
Print('la suma de los numeros introducidoses:', suma )
Print('el cuadrado de la suma de los valores es: ' ,cuadrado)
Print('el promedio de la suma de los valores es:',promedio)
Print('el menor número introducido es:', mínimo)