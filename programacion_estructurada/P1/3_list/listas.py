import os
#Ejemplo 1 Crear una lista de numeros e imprimir el contenido

os.system("cls")

numeros = [10, 19, 30, 40]
#1er Forma
print(numeros)

#2da Forma Valor
for i in numeros:
    print(i)

#3er Forma Indices
for i in range(0, len(numeros)):
    print(numeros[i])



#Ejemplo 2 Crear una lista de palabras y posteriormente buscar la concidencia de una palabra
os.system("cls")

palabras = ["Barcelona","PSG","Inter Miami","Argentina"]
palabra_buscar = input("Dame la palabra a buscar: ")

#1er Forma
if palabra_buscar in palabras:
    print("Si se encontró la palabra")
else:
    print("No se encontró la palabra")


#2da Forma
encontro = False
for i in palabras:
    if i == palabra_buscar:
        encontro = True

if encontro:
    print("Si se encontró la palabra")
else:
    print("No se encontró la palabra")


#3er Forma
encontro = False
for i in range(0, len(numeros)):
    if palabras[i] == palabra_buscar:
        encontro = True

if encontro:
    print("Si se encontró la palabra")
else:
    print("No se encontró la palabra")





#Añadir elementos a la lista
os.system("cls")
numeros = []

resp = "SI"
while resp == "SI":
    numeros.append(float(input("Dame un numero entero o decimal: ")))
    resp = input("¿Deseas agreagra otra palabra o elemento?(Si/No): ").upper()

print(numeros)


#Ejemplo 4 Crear una lista multidimensional (matriz) que almacene el nombre y telefono de 4 personas
os.system("cls")

agenda = [
    ["Ana", "618-878-69-74"],
    ["Eduardo", "618-741-52-74"],
    ["Leo", "618-752-02-32"],
    ["Carlos", "618-521-74-65"]
]

#print(agenda)


for r in agenda:
   print(r)

for r in range(0, 3):
   for c in range(0, 2):
      print(agenda[r][c])

valores = ""
for r in range(0, 3):
    for c in range(0, 2):
        valores += f"[{agenda[r][c]}]"
    valores += "\n"
print(valores)
