import os
import mysql.connector
from mysql.connector import Error

pelicula = {}

def esperarTecla():
    input("\n\t...Oprime cualquier tecla para continuar...")

def borrarPantalla():
    os.system("cls")

def conectar():
    try:
        conexion = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "",
            database = "bd_peliculas"
        )
        return conexion
    except Error as e:
        print(f"El error que se presento es: {e}")
        return None

def agregarPeliculas():
    borrarPantalla()
    conexionBD = conectar()
    if conexionBD != None:
        print("\t\t 🎬 .::Agregar Película::. 🎬\n")
    
        pelicula["nombre"] = input("Ingresa el Nombre: ").upper().strip()
        #pelicula.update({"nombre": input("Ingresa el Nombre: ").upper().strip()})
        pelicula.update({"categoria": input("Ingresa la Categoria: ").upper().strip()})
        pelicula.update({"clasificacion": input("Ingresa la Clasificacion: ").upper().strip()})
        pelicula.update({"genero": input("Ingresa el genero: ").upper().strip()})
        pelicula.update({"idioma": input("Ingresa el Idioma: ").upper().strip()})
    
        cursor = conexionBD.cursor()

        sql = "INSERT INTO peliculas (nombre, categoria, clasificacion, genero, idioma) VALUES (%s, %s, %s, %s, %s)"
        valores = (pelicula["nombre"], pelicula["categoria"], pelicula["clasificacion"], pelicula["genero"], pelicula["idioma"])
        cursor.execute(sql, valores)
        conexionBD.commit()

        print("\n\t✅ .::La película se ha guardado en la base de datos::. ✅")
        cursor.close()

def borrarPeliculas():
    borrarPantalla()
    conexionBD = conectar()
    if conexionBD != None:
        print("\t\t🔍 .::Borrar Peliculas::. 🔍\n")

        nombre = input("Ingresa el nombre de la pelicula a borrar: ").upper().strip()

        cursor = conexionBD.cursor()
        sql = "SELECT * FROM peliculas WHERE nombre = %s"
        val = (nombre,)
        cursor.execute(sql, val)
        registros = cursor.fetchall()

        if registros:
            print("\n\t::Mostrar las películas::.")
            print(f"{'ID':<10} {'Nombre':<15} {'Categoria':<15} {'Clasificación':<15} {'Género':<15} {'Idioma':<15}")
            print(f"-" * 80)
            for peli in registros:
                print(f"{peli[0]:<10}{peli[1]:<15}{peli[2]:<15}{peli[3]:<15}{peli[4]:<15}{peli[5]:<15}")
                print(f"-" * 80)
                resp = input(f"¿Deseas borrar la película {nombre}? (Si/No): ").upper().strip()
                if resp == "SI":
                    sql = "DELETE FROM peliculas WHERE nombre = %s"
                    val = (nombre,)
                    cursor.execute(sql, val)
                    conexionBD.commit()
                    print("\n\t✅ .::La película se ha borrado de la base de datos::. ✅")
        else:
            print("\n\t❌ .::Películas no encontradas en el sistema::. ❌")
    
def mostrarPeliculas():
    borrarPantalla()
    conexionBD = conectar()
    if conexionBD != None:
        print("\t\t🎞 .::Mostrar las Peliculas::. 🎞\n")
    
        cursor = conexionBD.cursor()
        sql = "SELECT * FROM peliculas"
        cursor.execute(sql)
        registros = cursor.fetchall()
    
        if registros:
            print("\n\t::Mostrar las películas::.")
            print(f"{'ID':<10} {'Nombre':<15} {'Categoria':<15} {'Clasificación':<15} {'Género':<15} {'Idioma':<15}")
            print(f"-" * 80)
            for peli in registros:
                print(f"{peli[0]:<10}{peli[1]:<15}{peli[2]:<15}{peli[3]:<15}{peli[4]:<15}{peli[5]:<15}")
                print(f"-" * 80)
        else:
            print("\n\t❌ .::No hay películas en la base de datos::. ❌")

        cursor.close()

def buscarPeliculas():
    borrarPantalla()
    conexionBD = conectar()
    if conexionBD != None:
        print("\t\t🔍 .::Buscar Peliculas::. 🔍\n")

        nombre = input("Ingresa el nombre de la pelicula a buscar: ").upper().strip()

        cursor = conexionBD.cursor()
        sql = "SELECT * FROM peliculas WHERE nombre = %s"
        val = (nombre,)
        cursor.execute(sql, val)
        registros = cursor.fetchall()

        if registros:
            print("\n\t::Mostrar las películas::.")
            print(f"{'ID':<10} {'Nombre':<15} {'Categoria':<15} {'Clasificación':<15} {'Género':<15} {'Idioma':<15}")
            print(f"-" * 80)
            for peli in registros:
                print(f"{peli[0]:<10}{peli[1]:<15}{peli[2]:<15}{peli[3]:<15}{peli[4]:<15}{peli[5]:<15}")
                print(f"-" * 80)
        else:
            print("\n\t❌ .::Películas no encontradas en el sistema::. ❌")
    
def ModificarPeliculas():
    borrarPantalla()
    conexionBD = conectar()
    if conexionBD != None:
        print("\n\t🎥 .::Modificar Película::. 🎥\n")

        nombre = input("Ingresa el nombre de la pelicula a Modificar: ").upper().strip()

        cursor = conexionBD.cursor()
        sql = "SELECT * FROM peliculas WHERE nombre = %s"
        val = (nombre,)
        cursor.execute(sql, val)
        registros = cursor.fetchall()

        if registros:
            print("\n\t::Películas::.")
            print(f"{'ID':<10} {'Nombre':<15} {'Categoria':<15} {'Clasificación':<15} {'Género':<15} {'Idioma':<15}")
            print(f"-" * 80)
            for peli in registros:
                print(f"{peli[0]:<10}{peli[1]:<15}{peli[2]:<15}{peli[3]:<15}{peli[4]:<15}{peli[5]:<15}")
                print(f"-" * 80)
                resp = input(f"¿Deseas Modificar la película {nombre}? (Si/No): ").upper().strip()
                if resp == "SI":
                    pelicula["nombre"] = input("Ingresa el Nombre: ").upper().strip()
                    #pelicula.update({"nombre": input("Ingresa el Nombre: ").upper().strip()})
                    pelicula.update({"categoria": input("Ingresa la Categoria: ").upper().strip()})
                    pelicula.update({"clasificacion": input("Ingresa la Clasificacion: ").upper().strip()})
                    pelicula.update({"genero": input("Ingresa el genero: ").upper().strip()})
                    pelicula.update({"idioma": input("Ingresa el Idioma: ").upper().strip()})

                    sql = "UPDATE peliculas SET nombre = %s, categoria = %s, clasificacion = %s, genero = %s, idioma = %s WHERE nombre = %s"
                    val = (pelicula["nombre"], pelicula["categoria"], pelicula["clasificacion"], pelicula["genero"], pelicula["idioma"], nombre)
                    cursor.execute(sql, val)
                    conexionBD.commit()
                    print("\n\t✅ .::La película se ha modificado en la base de datos::. ✅")
        else:
            print("\n\t❌ .::Películas no encontradas en el sistema::. ❌")
