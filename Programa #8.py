casillaActual=0
casillaSiguiente=0
for i in range (0,63):
	casillaActual+=2
	casillaSiguiente+=casillaActual

Peso=(casillaSiguiente+1)*1.3
print('El peso de cada grano es de: 1.3 Gramos.')	
print('La cantidad de granos que obtendra el creador de el juedo es: ',casillaSiguiente+1,'granos.')
print('El peso resultante de la cantidad de granos es de:'+str(round(Peso,2)),'Gramos')