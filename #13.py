for i in range(5):
	a=int(input('Ingrese un numero: '))
	b=int(input('Ingrese el segundo numero: '))
	a2=a**2
	b2=b**2
	c2=(a2+b2)
	c=c2**0.5
	print(a,'² +',b,'² ='+str(round(c)),'²')
	print(a2,'+',b2,'=',c2)
	print()