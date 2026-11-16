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


