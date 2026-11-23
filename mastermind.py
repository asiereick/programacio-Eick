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
        jugada.append(int(input("escrive tu jugada: ")))
    print("\n""tu jugada es:",jugada, "\n")


    



    Correctas=[]
    for i in range(len(jugada)):
        if jugada[i] == ns[i]:
            Correctas.append(jugada[i])

     
    if Correctas == ns:
        intent += 11
        print("\nfelicidades, has descubierto el codigo", Correctas )
        print("\n")
    else: 
        print("Jugadas correctas:""\n")   
        if Correctas == []:
            print("no hay jugadas correctas""\n")
        else:
            
            print(Correctas)
            print("")

    

        casi=[]
        for i in range(len(jugada)):
            if jugada[i] in ns and jugada[i] != ns[i]:
                casi.append(jugada[i])

        print("jugadas en otra posicion:""\n")
        if casi == []:
            print("no hay jugadas en posiciones equivocadas" "\n")
        else:
            print(casi)
            print("")




        erronias=[]
        for i in range(len(jugada)):
            if jugada[i] not in ns:
                erronias.append(jugada[i])

        print("jugadas erronias:""\n")
        if erronias == []:
            print("no hay jugadas erronias""\n")
        else:
            print(erronias )
            print("")

if intent == 10:
    print("no has descubierto el codigo en 10 intentos, reinicia y prueba otro")
    print("")