'''
Proyecto 1

Crear un proyecto que permita gestionar (administrar) peliculas; colocar un menu de opciones para agregar, borrar, modificar,
consultar, buscar peliculas.
Notas:
1.- Utilizar funciones y mandar llamar desde otro archivo
2.- Utilizar una dict para almacenar los atributos o caracteristicas de las peliculas (nombre, categoria, clasificacion, genero, idioma)
3.- Utilizar e implementar una BD relacional en MySQL
'''

import peliculas


op = True
while op:
    peliculas.borrarPantalla()
    print("\t\t🍿 CINEPOSLIS CLON 🍿\n\tSelcciona una opcion para empezar:\n\n\t 1️⃣  Crear una pelicula\n\t 2️⃣  Borrar un pelicula\n\t 3️⃣  Mostrar una pelicula\n\t 4️⃣  Buscar Pelicula\n\t 5️⃣  Modificar Pelicula\n\t 6️⃣  Salir")

    op = input("\n👉 Opcion seleccionada: ").upper()
    match op:
        case "1":
            peliculas.agregarPeliculas()
            peliculas.esperarTecla()
        case "2":
            peliculas.borrarPeliculas()
            peliculas.esperarTecla()
        case "3":
            peliculas.mostrarPeliculas()
            peliculas.esperarTecla()
        case "4":
            peliculas.buscarPeliculas()
            peliculas.esperarTecla()
        case "5":
            peliculas.ModificarPeliculas()
            peliculas.esperarTecla()
        case "6":
            peliculas.borrarPantalla()
            print("🚪 .::Terminaste de usar el programa::. 🚪")
            op = False
        case _:
            op = True
            input("❌ Opcion no valida, vuelva a intentarlo ❌")