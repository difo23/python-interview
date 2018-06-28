print('empresa')
           
x=int (input("dijite las horas que a trabajado en una semana "))
xx=int (input("dijite su sueldo por hora "))
a=0
c=0
d1=0
d2=0
d3=0
f1=0
f2=0
f3=0
f4=0
z1=0
z2=0
z3=0
result1=0
result2=0
result3=0

if (x>40):
    c=xx*1.5
    a=x*c
    f1=a
    f2=a
   
    print ('el sueldo bruto es de: ',a)
  
else:
     a=x*xx
     f1=a
     f2=a
    
     
     print ('el sueldo bruto es de: ',a)
    
while True:
    f1-=1
   
    if (f1==1100):
        d1=f1
        break
    
while True:
    f2-=1
    f3+=1
    if (f2==1500):
        d2=f2
        break

z1=d1*0.10
z2=d2*0.15
f4=f3-d1


z3=f4*0.25

result1=d1-z1
result2=d2-z2
result3=f4-z3

print ('El 10% de retencion primeros 1100 es: ',result1)
print ('El 15% de retencion de los siguientes 1500 es: ',result2)

print ('El 25% de retencion del  resto del dinero es: ',result1)

print ('El sueldo neto es: ',result1+result2+result2)
