salario = int(input("Introduce el salario por hora\n(El salario minimo por hora es 261$RD)"))
horas_tranajadas = int(input("Introduce la cantidad de horas trabajadas por semana"))

salario_extra = 0
salario_neto = 0
horas_extra = 0
retencion = 110
retencion_2 = 225

while salario >= 261:
    for i in range(horas_tranajadas, 40, -1):
        horas_tranajadas -= 1
        horas_extra += 1

    if horas_extra != 0:\
        salario_extra = (salario*horas_extra*1.5)

    salario_neto = salario*horas_tranajadas
    retencion_3 = (salario_neto-2852)*0.25
    retenciones = (retencion+retencion_2+retencion_3)

    if horas_extra > 0:
        print("Su salario neto es: %s$RD\nMas las horas extras %sRD\nPara un total de %s$RD" %(salario_neto, salario_extra, (salario_neto+salario_extra)))
        salario_neto += salario_extra

    else:
        print("Su sueldo neto es: %s$RD y no trabajo horas extra" %(salario_neto))

    print("Retenciones\n10% de los primeros 1100$RD " + str(retencion) + "$RD\n15% de los 1500$RD " + str(retencion_2) + "$RD\n25% de lo restante " + str(retencion_3) + "$RD")
    print("Tiene %s$RD en Retenciones" %(retenciones))
    print("Su sueldo base es de: %s$RD" %(salario_neto - (retenciones)))
    break
if salario < 261:
    print("Ese salario esta por debajo del salario minimo, intentelo nuevamente.")
print("Fin del Programa")