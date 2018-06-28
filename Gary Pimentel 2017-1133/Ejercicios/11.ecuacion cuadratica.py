import math
print("Resolvedor de ecuaciones con la formula general")
def ecuacion(a,b,c):
    a = float(a)
    b = float(b)
    c = float(c)
    comprobaerrores = (b**2)-(4*a*c)
    if comprobaerrores == 0:
        resub = 0
        solucion1 = -(b)/2*a
        print("El resultado es %d" %solucion1)

    if comprobaerrores > 0:
        comprobaerrores = math.sqrt(comprobaerrores)
        solucion1 = -(b)+comprobaerrores/2*a
        solucion2 = -(b)-comprobaerrores/2*a
        print("El resultado son:\ndel lado positivo %d\ndel lado negativo %d" %(solucion1,solucion2))
    if comprobaerrores < 0:
        print("Da error por tener numero negativo, se quedaria asi -(%d)+-raiz de%d/2*%d" %(b,comprobaerrores,a))


ecuacion(2,3,6)
ecuacion(5,0,0)
ecuacion(1,6,5)
ecuacion(5,-30,0)