
tabla=[]
num=int(input("Escribe un numero"))
for i in range (1,21):
    num = int(input("Escribe un numero"))
    tabla.append(num)
print(tabla)
num2=int(input("Escribe el numero a buscar"))
repetidos=tabla.count(num2)


print("el",num2,"se ecuentra repetido",repetidos,"veces", end= " ")
