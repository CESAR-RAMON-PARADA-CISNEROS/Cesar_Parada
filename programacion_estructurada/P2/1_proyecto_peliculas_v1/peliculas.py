import os

peliculass = []

def borrarPantalla():
    os.system("cls")

def esperarTecla():
    input("\n\t...Oprima una tecla para continuar...")

def agregarPelicula():
    borrarPantalla()
    print("\t\t.::Agregar peliculas::.\n")
    peli = input("¿Que pelicula desea agregar a la lista?: ").upper().strip()
    peliculass.append(peli)
    print("\n\t.::LA OPERACION SE REALIZO CON EXITO::.")

def borrarPelicula():
    borrarPantalla()
    print("\t\t.::Borrar peliculas::.\n")
    peli = input("Ingresa la pelicula que desea borrar de la lista: ").upper().strip()
    encontro = 0
    if not (peli in peliculass):
        print("\n\t ::¡No se encuentra la pelicula!::")
    else:
        resp = "SI"
        while peli in peliculass and resp == "SI":
            resp = input("¿Deseas borrar la pelicula del sistema? (Si/No): ").upper().strip()
            if resp == "SI":
                posicion = peliculass.index(peli)
                print(f"\nLa pelicula que se borro es {peli} y estaba y esta en la casilla {posicion + 1}")
                peliculass.remove(peli)
                encontro += 1
                input("\n\t.::LA OPERACION SE REALIZO CON EXITO::.")
        print(f"\n\t::Se borro {encontro} la pelicula(s) con este titulo")

def modificarPelicula():
   borrarPantalla()
   print("\n\t.:: Modificar Películas ::. \n")
   peli =input("Ingrese el nombre de la película que desea buscar: ").upper().strip()
   encontro=0
   if not(peli in peliculass): 
      print("\n\t\t ¡No se encuentra la película a buscar!")   
   else:   
      for i in range(0,len(peliculass)):
        if peli==peliculass[i]:
          resp=input("¿Deseas actualizar la pelicula? (Si/No) ").lower()
          if resp=="si":
             peliculass[i]=input("\nIntroduce el nuevo nombre de la película: ").upper().strip()
             encontro+=1
             print("\n\t\t::: ¡LA OPERACION SE REALIZO CON ÉXITO! :::")
      
      print(f"\nSe modifico {encontro} pelicula(s) con este titulo")  

def consultarPeliculas():
    borrarPantalla()
    print("\t\t.::Consultar peliculas::.\n")
    if len(peliculass) > 0:
        for i in range(0, len(peliculass)):
            print(f"{i + 1} : {peliculass[i]}")
    else:
        print("\n\t .::No hay películas en el Sistema en este momento::.")

def buscarPelicula():
    borrarPantalla()
    print("\t\t.::Buscar peliculas::.\n")
    peli = input("¿Que pelicula desea buscar en la lista?: ").upper().strip()
    encontro = 0
    if not (peli in peliculass):
        print("\n\t ::¡No se encuentra la pelicula!::")
    else:
        for i in range(0, len(peliculass)):
            if peli == peliculass[i]:
                print(f"\nLa pelicula {peli} si se encontro y esta en la casilla {i + 1}")
                encontro += 1
        print(f"\n::Tenemos {encontro} pelicula(s) con este titulo::")
        ("\n\t.::LA OPERACION SE REALIZO CON EXITO::.")

def vaciarPeliculas():
    borrarPantalla()
    print("\t\t.::Vaciar peliculas::.\n")
    resp = input("¿Deseas borrar todas las peliculas del sistema? (Si/No): ").upper().strip()
    if resp == "SI":
        peliculass.clear()
        print(".::LA OPERACION SE REALIZO CON EXITO::.")