def granosTrigo(trigo):
    if trigo == 0 or trigo == 1:
        return 1
    
    else:
        return 2**trigo-1

peso = 0.25
pesoTrigo=(granosTrigo(64)*peso)
longitud = str(pesoTrigo)

print("Se tienen %d granos de trigo." %(granosTrigo(64)))
print("Que pesan aproximadamente %d gramos"%(pesoTrigo)) 
print("Se necesitan %s bits para escribir el peso de los gramos de trigo" %(len(longitud) - 2))