horaTrabajada = int(input("Introduces las horas trabajadas por semanas"))
salarioHora = int(input("Introduce el Salario por hora de un empleado en $RD \nSueldo minimo 200 $RD"))

horaExtras = 0
sueldoBruto = 0
salarioExtra = 0
restrincion = 110   
restrincion2 = 225   

while salarioHora >= 200:
    for i in range(horaTrabajada, 40, -1):
        horaTrabajada -= 1
        horaExtras += 1

    if horaExtras != 0:
        salarioExtra = (salarioHora * 1.5 * horaExtras)

    sueldoBruto = horaTrabajada * salarioHora
    restrincion3 = (sueldoBruto-2600)*0.25   

    if horaExtras > 0:                       
        print("Su sueldo bruto es de %d $RD mas %d $RD horas extras \nUn total de %d $RD"
              % (sueldoBruto, salarioExtra, (sueldoBruto+salarioExtra)))
        sueldoBruto += salarioExtra

    else:
        print("Su sueldo bruto es: %d $RD. No trabajo hora extras esta semana" % sueldoBruto)

    print(" Retenciones: \n10% de los primeros RD$1100 " + str(restrincion) + "$RD \n15% de los 1500 siguientes "
          + str(restrincion2) + "$RD \n25% del resto." + str(restrincion3) + "$RD")

    print("Tiene un total de %d $RD retenciones" % (restrincion+restrincion2+restrincion3))
    print("Su sueldo neto es igual a: %d $RD" % (sueldoBruto-(restrincion+restrincion2+restrincion3)))
    break
if salarioHora < 200:
    print("Error!! \nEl sueldo minimo es 200 $RD la hora")
