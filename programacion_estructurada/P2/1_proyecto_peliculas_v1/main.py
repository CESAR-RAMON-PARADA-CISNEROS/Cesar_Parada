'''
Proyecto 1

Crear un proyecto que permita gestionar (administrar) peliculas; colocar un menu de opciones para agregar, borrar, modificar,
consultar, buscar y vaciar peliculas.
Notas:
1.- Utilizar funciones y mandar llamar desde otro archivo
2.- Utilizar una lista para almacenar los nombres de las peliculas
'''

import peliculas


op = True
while op:
    peliculas.borrarPantalla()
    print("\t\tBIENVENIDO AL GESTOR DE CINE:\n\tSelcciona una opcion para empezar:\n\n\t1.- Agregar una pelicula\n\t2.- Borrar un pelicula\n\t3.- Modificar una pelicula\n\t4.- Mostrar las peliculas\n\t5.- Buscar un pelicula\n\t6.- Limpiar peliculas\n\t7.- Salir")

    op = input("\n Opcion seleccionada: ").upper()
    match op:
        case "1":
            peliculas.agregarPelicula()
            peliculas.esperarTecla()
        case "2":
            peliculas.borrarPelicula()
            peliculas.esperarTecla()
        case "3":
            peliculas.modificarPelicula()
            peliculas.esperarTecla()
        case "4":
            peliculas.consultarPeliculas()
            peliculas.esperarTecla()
        case "5":
            peliculas.buscarPelicula()
            peliculas.esperarTecla()
        case "6":
            peliculas.vaciarPeliculas()
            peliculas.esperarTecla()
        case "7":
            peliculas.borrarPantalla()
            print(".::Terminaste de usar el programa::.")
            op = False
        case _:
            op = True
            input("Opcion no valida, vuelva a intentarlo")