import random
ns=[]
for i in range(4):
    ns.append(random.randint(1,6))

#para pruebas viendo el codigo
print(ns) 
#
print("")

print("reglas: escrive 4 numeros del 1 al 6 sin repetir numeros. " \
"Los numeros que escrivas canviaran a:" \
"'C' esta en la posicion correcta" \
"'O' es que esta en otra posicion"
"'X' no esta en el codigo")

max=input("que dificultad quieres: F son 10 intentos, M son 6 y D son 3: ")

if max == "F":
    max = 10
if max == "M":
    max = 6
if max == "D":
    max = 3




intent=0
while (intent<max):
    print("tienes", max-intent, "intentos restantes \n")
    intent+=1
    ju=[]

    ju = (input("escrive 4 numeros del 0 al 6 sin espacios: "))
    while len(ju) != 4 or any(num not in "123456" for num in ju):
        print("Introduce exactamente 4 dígitos del 1 al 6.")
    jugada = [int(num) for num in ju]
    print("tu jugada es:", jugada)

    if jugada == ns:
        intent += 11
        print("\nfelicidades, has descubierto el codigo", jugada )
        print("\n")

    else:

        for i in range(len(jugada)):

            if jugada[i] == ns[i]:
                 jugada[i] = "C"

            if jugada[i] in ns and jugada[i] != ns[i]:
                jugada[i] = "O"

            if jugada[i] not in ns:
                jugada[i] = "X"

    
    
    
    


    
    

    

    



        
        



if intent == 10:
    print("no has descubierto el codigo en 10 intentos, reinicia y prueba otro")
    print("")