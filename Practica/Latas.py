print("Veamos que cantidad niveles de piramides de latas podemos hacer con x cantidad!")

l = int(input("Cuantas latas tienes?\n"))

def Can(l): 
    lvl_up = 0
    sobras = l

    for i in range(0, sobras, 2):

        if sobras >= i+1:
            lvl_up += 1
            sobras -= i+1

    print("Teniendo %s latas, se hacen %s niveles y quedan %s latas" % (l, lvl_up, sobras))

Can(l)


