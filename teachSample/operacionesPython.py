for i in range(10):
    if not i % 2 == 0:
   	    print(i+1)

print(((3**4)+(35//4))/8%6) #5.125
print((4**2) and (0) or (20//5)) # 4

#Nota esta operacion resulta interesante y deben estudiarla para entenderla:

"""
0= False
n> 0 <n es True
and y or evalúan una expresión de izquierda a derecha.
La operación and, si todos los valores son True, retorna el último en ser evaluado. Si algún valor es falso, retorna el primero.
or retorna el primer valor que sea True. Si todos son False, retorna el último.
Operador	Descripción
not x	Retorna True si x es True; False en caso contrario.
x and y	Retorna x si x es False; y en caso contrario.
x or y	Retorna y si x es False; x en caso contrario.
"""

print(3>=4 or 3>3 and 2>2) #False

a=8
b=10
c=8
d=[8,2,3,10,5]

print((a is b and a is not c) or b not in d) #false
print((a is c or b in d) or a < d[3]) #true
print(a/d[1]) #4.0 
print((b & d[2])>>2) # 0
print(d[2]<<3)# 24
print(d[2]/c)# 0.375
print(b != d[3])# False