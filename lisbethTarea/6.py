print('banco digital')
i=0
c=1000
print('libreta de ahorro ',c) 
x=int(input('dijite el monto que desea ahorrar: '))
y=int(input('ingrese la tasa de interes: '))
z=int(input('meses de ahorro: '))

for i in range(z):
            c=c+y
print('monto final: ',x+c)              
