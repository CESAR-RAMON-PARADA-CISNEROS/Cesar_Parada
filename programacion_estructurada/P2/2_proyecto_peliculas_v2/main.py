'''
Proyecto 1

Crear un proyecto que permita gestionar (administrar) peliculas; colocar un menu de opciones para agregar, borrar, modificar,
consultar, buscar y vaciar peliculas.
Notas:
1.- Utilizar funciones y mandar llamar desde otro archivo
2.- Utilizar una dict para almacenar los atributos o caracteristicas de las peliculas (nombre, categoria, clasificacion, genero, idioma)
'''

import peliculas


op = True
while op:
    peliculas.borrarPantalla()
    print("\t\tBIENVENIDO AL GESTOR DE CINE:\n\tSelcciona una opcion para empezar:\n\n\t1.- Crear una pelicula\n\t2.- Borrar un pelicula\n\t3.- Mostrar una pelicula\n\t4.- Agregar caracteristica\n\t5.- Modificar Caracteristica\n\t6.- Borrar Caracteristica\n\t7.- Salir")

    op = input("\n Opcion seleccionada: ").upper()
    match op:
        case "1":
            peliculas.crearPeliculas()
            peliculas.esperarTecla()
        case "2":
            peliculas.borrarPeliculas()
            peliculas.esperarTecla()
        case "3":
            peliculas.mostrarPeliculas()
            peliculas.esperarTecla()
        case "4":
            peliculas.agregarCaracteristicaPeliculas()
            peliculas.esperarTecla()
        case "5":
            peliculas.ModificarCaracteristicaPeliculas()
            peliculas.esperarTecla()
        case "6":
            peliculas.borrarCaracteristicaPeliculas()
            peliculas.esperarTecla()
        case "7":
            peliculas.borrarPantalla()
            print(".::Terminaste de usar el programa::.")
            op = False
        case _:
            op = True
            input("Opcion no valida, vuelva a intentarlo")