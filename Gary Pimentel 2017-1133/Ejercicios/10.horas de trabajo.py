print("Bienvenidos a la hora feliz, el pago")
print("Para poder cobrar necesitara tener mas de 30 horas de trabajo en la semana")
horas = int(input("Digite las horas que trabaja en la semana: "))
salario = int(input("Digite el salario que gana por hora: "))
memoradum = int(input("Cuantos memoradum ha tenido: "))
horasextras = int(input("Cuantas horas extras a trabajado: "))
horaextra = 1.5
pago = 0
cargos = 50
impuestos = 1200
if horas > 30 and horaextra > 0 and memoradum > 0:
    horas = horas*salario
    horaextra = horasextras*horaextra
    horaextra = horaextra*horas
    memoradum = cargos*memoradum
    pago = horaextra-impuestos
    pago -= memoradum
    print("El empleado cobrara RD$%d pesos" %pago)
elif horas > 30 and memoradum > 0:
    horas = horas*salario
    memoradum = cargos*memoradum
    pago = horas-impuestos
    pago -= memoradum
    print("El empleado cobrara RD$%d pesos" %pago)
elif horas > 30:
    horas = horas*salario
    pago = horas-impuestos
    print("El empleado cobrara RD$%d pesos" %pago)
else:
    print("No cumplio los requisitos de la empresa para pagarle")
        