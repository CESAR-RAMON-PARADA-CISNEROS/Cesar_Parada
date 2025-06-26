import os

#lista = [
#    ["Ruben", 10.0, 10.0, 10.0]
#    ["Diana", 10.0, 9.8, 8.0]
#    ["Ruben", 5.0, 6.0, 7.0]
#]

def borrarPantalla():
    os.system("cls")

def esperarTecla():
    input("\n\t...Oprima una tecla para continuar...")

def menu_principal():
    print("\t\t📂SISTEMA DE GESTIÓN DE CALIFICACIONES📂:\n\tSelcciona una opcion para empezar:\n\n\t1.- Agregar\n\t2.- Mostrar\n\t3.- Calcular promedio\n\t4.- Salir")
    op = input("\n Opcion seleccionada: ").upper().strip()
    return op

def agregarCalificaciones(lista):
    borrarPantalla()
    print("📝 .::Agregar Calificaciones::. 📝")
    nombre=input("Nombre del Alumno: ").upper().strip()
    calificaciones=[]
    for i in range(1,4):
        continua=True
        while continua:
            try:
                cal=float(input(f"Calificación {i}: "))
                if cal>=0 and cal<11:
                    calificaciones.append(cal)
                    continua=False
                else:
                    print("Ingresa un número valido") 
            except ValueError:
                print("Ingresa un valor númerico")
    lista.append([nombre]+calificaciones)
    print("✅ Acción realizada con exíto ✅")

def mostrarCalificaciones(lista):
    borrarPantalla()
    print("📝 .::Mostrar Calificaciones::. 📝") 
    if len(lista)>0:
        print(f"{'Nombre':<15}{'Calf. 1':<10}{'Calf. 2':<10}{'Calf. 3':<10}")
        print(f"{'-'*40}")
        for fila in lista:
            print(f"{fila[0]:<15}{fila[1]:<10}{fila[2]:<10}{fila[3]:<10}")
        print(f"{'-'*40}")  
        cuantos=len(lista)
        print(f"Son {cuantos} alumnos")
    else:
      print("⚠️ No hay calificaciones registradas en el sistema ⚠️")

def calcularPromedios(lista):
    borrarPantalla()
    print("📝 .:: PROMEDIOS ::. 📝")
    if len(lista)>0:
        print(f"{'Alumno':<15}{'Promedio':<10}")
        print(f"{'-'*30}")
        promedio_grupal=0
        for fila in lista:
            nombre=fila[0]
            promedio=sum(fila[1:])/3
            print(f"{nombre:<15}{promedio:.2f}")  
            promedio_grupal+=promedio 
        print(f"{'-'*30}")
        promedio_grupal=promedio_grupal/len(lista)
        print(f"El promedio grupal es: {promedio_grupal} ")
    else:
      print("⚠️ No hay calificaciones registradas en el sistema ⚠️")
        
