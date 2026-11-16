'''while True:
    print("hola")
'''

# programa donde el usuario escrive 3 numeros y el programa los reescrive al final

nombre=[]
for i in range(3):
    nombre.append((input("escrive un nombre: ")))
print("los nombres son:", nombre)

#contar las "a" que hay en el primer nombre
a=0
for i in nombre[0]:
    if i=="a":
        a+=1
print("as en", nombre[0],":", a)


for i in range(17, 101):
    if i%2==0:
        print(i,end=" ")

#programa que cuenta cuantos 10 hay en una lista 

notes=[[6,6,7,10,9],[10,7,6,7,7],[5,5,10,7,10]]
diez=0
for i in notes:
    for i in i:
        if(i==10):
            diez+=1
            print("hay", diez, "diezes")

#decir donde estan los 10 en la lista
for i in range(3):
    for j in range(5):
        if(notes[i][j]==10):
            print ("fila", i, "columna", j)

#programa que te pide adivinar un programa del 0 al 10 y no para hasta que lo adivines

print ("tienes queadivinar el numero del 0 al 10")
nume=0
while (nume != 7):
    nume=int(input("que numero cres que es?: "))
    if (nume != 7):
        print("nu hu, ese no era")
    if (nume==7):
        print("sip, es ese")