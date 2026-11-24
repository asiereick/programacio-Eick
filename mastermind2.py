import random
ns=[]
for i in range(4):
    ns = random.sample(range(1, 7), 4)

#para pruebas viendo el codigo
print(ns) 
#
print("")

print("reglas: escrive 4 numeros del 1 al 6 sin repetir numeros. ""\n" \
"Los numeros que escrivas canviaran a:""\n" \
"'C' esta en la posicion correcta""\n" \
"'O' es que esta en otra posicion""\n"
"'X' no esta en el codigo")

max=input("\n""que dificultad quieres: F son 10 intentos, M son 6 y D son 3: ")

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

    ju = (input("escrive 4 numeros del 1 al 6 sin espacios: "))
    if len(ju) != 4 or any(num not in "123456" for num in ju):
        print("Introduce exactamente 4 dígitos del 1 al 6.")

    jugada = [int(num) for num in ju]
    
    print("\n")
    if jugada == ns:
        intent += 11
        print("\nfelicidades, has descubierto el codigo", jugada )
        print("\n")

    else:


        resultado=[]
        for i in range(len(jugada)):
            if jugada[i] == ns[i]:
                 resultado.append("C")

        
            elif jugada[i] in ns and jugada[i] != ns[i]:
                resultado.append("O")

        
            else:
                resultado.append("X")

        print("la jugada", jugada, "es",resultado)
        print("\n")


if intent == 10:
    print("no has descubierto el codigo en 10 intentos, reinicia y prueba otro")
    print("")