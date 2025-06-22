import os

#dict u objeto para almacenar los atributos (nombre, categoria, calsificacion, genero, idioma) y sus valores

#peliculass = {
#        "Nombre":"",
#        "Categoria":"",
#        "Clasificacion":"",
#        "Genero":"",
#        "Idioma":""
#}

pelicula = {}


def borrarPantalla():
    os.system("cls")

def esperarTecla():
    input("\n\t...Oprima una tecla para continuar...")

def crearPeliculas():
    borrarPantalla()
    print("\t\t.::Crear peliculas::.\n")
    #pelicula["Nombre"] = input("Ingresa el Nombre: ").upper().strip()
    pelicula.update({"nombre": input("Ingresa el Nombre: ").upper().strip()})
    pelicula.update({"categoria": input("Ingresa la Categoria: ").upper().strip()})
    pelicula.update({"clasificacion": input("Ingresa la Clasificacion: ").upper().strip()})
    pelicula.update({"genero": input("Ingresa el genero: ").upper().strip()})
    pelicula.update({"idioma": input("Ingresa el Idioma: ").upper().strip()})
    print("\n\t.::LA OPERACION SE REALIZO CON EXITO::.")

def borrarPeliculas():
    borrarPantalla()
    resp = input("¿Deseas borrar todas las peliculas? (Si/No): ").upper().strip()
    if resp == "SI":
        pelicula.clear()
        print("\n\t.::LA OPERACION SE REALIZO CON EXITO::.")

def mostrarPeliculas():
    borrarPantalla()
    print("\t\t.::Mostrar las caracteristicas de Peliculas::.\n")
    if len(pelicula) > 0:
        for i in pelicula:
            print(f"\t {i} : {pelicula[i]}")
    else:
        print("\n\t .::No hay películas en el Sistema en este momento::.")

def agregarCaracteristicaPeliculas():
    borrarPantalla()
    print("\t\t.::Agregar Caracteristica a Peliculas::.\n")
    atributo = input("Ingresa la nueva caracteristica de la pelicula: ").lower().strip()
    valor = input("Ingresa el valor de la caracteristica de la pelicula: ").upper().strip()
    pelicula.update({atributo:valor})
    print("\n\t.::LA OPERACION SE REALIZO CON EXITO::.")

def ModificarCaracteristicaPeliculas():
    borrarPantalla()
    print("\t\t.::Modificar Caracteristica a Peliculas::.\n")
    resp = input("¿Deseas modificar las caracteristicas de la pelicula? (Si/No): ").upper().strip()
    if resp == "SI":
        if len(pelicula) > 0:
            for i in pelicula:
                print(f"\t {i} : {pelicula[i]}")
                cambio = input(f"\t¿Desea modificar el valor de {i}?: ").upper().strip()
                if cambio == "SI":
                    pelicula[i] = input("\n\tIngrese el nuevo valor: ").upper().strip()
                    print("\n\t.::LA OPERACION SE REALIZO CON EXITO::.")
        else:
            print("\n\t.::No hay peliculas en el Sistema::.")

def borrarCaracteristicaPeliculas():
    borrarPantalla()
    if len(pelicula) > 0:
        for i in pelicula:
            print(f"\t {i} : {pelicula[i]}")
        print("\n\t.::Estas son las caracteristicas de la pelicula::.")
        resp = input("\n\t¿Deseas borrar una caracteristica? (Si/No): ").upper().strip()
        if resp == "SI":
            eliminar = input("¿Que caracteristica desea eliminar?: ").lower().strip()
            if  not (eliminar in pelicula):
                input("\n\t.::No existe esa caracteristica::.")
            else:
                pelicula.pop(eliminar)
                print("\n\t.::LA OPERACION SE REALIZO CON EXITO::.")
    else:
        print("\n\t.::No hay peliculas en el Sistema::.")