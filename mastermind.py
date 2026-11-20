import random
ns=[]
for i in range(4):
    ns.append(random.randint(0,6))

#para pruebas viendo el codigo
print(ns) 
#
print("")


intent=0
while (intent<10):
    print("tienes", 10-intent, "intentos restantes \n")
    intent+=1
    jugada=[]
    for i in range(4):
        jugada.append(input("escrive tu jugada: "))
    print("\n""tu jugada es:",jugada, "\n")



    Correctas=[]
    for i in range(len(jugada)):
        if jugada[i] == ns[i]:
            Correctas.append(jugada[i])

    print("Jugadas correctas:")
    for i in range(len(Correctas)):
        print(Correctas[i]) 
    if Correctas == ns:
        print("todas son correctas")
        intent+=10
        print("\nfelicidades, has descubierto el codigo", Correctas )
        print("\n")
    else:
        print(Correctas)



    casi=[]
    if jugada[i] in ns[i]:
        casi.append(jugada[i])

    print("jugadas en otra posicion:")
    if jugada[i] in ns[i]:
        print(casi)




    erronias=[]
    for i in range(len(jugada)):
        if jugada[i] not in ns:
            erronias.append(jugada[i])

    print("jugadas erronias:")
    if jugada[i] not in ns:
        print(erronias)