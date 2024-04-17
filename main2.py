def omelete():
    ovos = 12 #"Variável local de omelete"
    print("Ovos = ", ovos)

def bacon ():
    ovos = 6 #"Variável local de bacon"
    print("Ovos =", ovos)
    omelete()
    print("Ovos =", ovos)

#Programa Principal
ovos = 2 #"Variável global"
bacon()
print("Ovos =", ovos)
