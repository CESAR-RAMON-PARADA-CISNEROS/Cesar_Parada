def borrarPantalla():
    import os
    os.system("cls")

def esperarTecla():
    input("\n\t...Oprima una tecla para continuar...")

def menu_principal():
    print("\t\t📅...:::Sistema de Gestión de Agenda de Contactos :::...📅\n\tSelcciona una opcion para empezar:\n\n\t 1️⃣  Agregar contacto\n\t 2️⃣  Mostrar contactos\n\t 3️⃣  Buscar contacto\n\t 4️⃣  Modificar contacto\n\t 5️⃣  Eliminar contacto\n\t 6️⃣  SALIR")
    op = input("\n👉 Elige una opción (1-6): ").upper().strip()
    return op

def agregarContacto(agenda):
    borrarPantalla()
    print("📝.:: Agregar Contacto ::.📝")
    nombre = input("\nNombre: ").upper().strip()
    if nombre in agenda:
        print("\n⚠ Contacto ya existente ⚠")
    else:
        telefono = input("Teléfono: ").strip()
        email = input("Email: ").upper().strip()
        agenda[nombre] = [telefono, email]
        print("\n✅ :: Acción realizada con éxito :: ✅")

def mostrarContactos(agenda):
    borrarPantalla()
    print("👤.:: Mostrar Contactos ::.👤")
    if not agenda:
        print("\n❌ ...No hay Contactos en la Agenda... ❌")
    else:
        print(f"\n{'Nombre':<15}{'Teléfono':<15}{'Email':<15}")
        print(f"-" * 60)
        for nombre, datos in agenda.items():
            print(f"{nombre:<15}{datos[0]:<15}{datos[1]:<15}")
        print(f"-" * 60)

def buscarContacto(agenda):
    borrarPantalla()
    print("🔍.:: Buscar Contacto ::.🔍")
    if not agenda:
        print("\n❌ ...No hay Contactos en la Agenda... ❌")
    else:
        nombre = input("\nNombre del contacto a buscar: ").upper().strip()
        if nombre in agenda:
           print(f"\n{'Nombre':<15}{'Teléfono':<15}{'Email':<15}")
           print(f"-" * 60)
           print(f"{nombre:<15}{agenda[nombre][0]:<15}{agenda[nombre][1]:<15}")
           print(f"-" * 60)
        else:
            print("\n❌ ...No existe el contacto... ❌")

def modificarContacto(agenda):
    borrarPantalla()
    print("🔄.:: Modificar Contacto ::.🔄")
    if not agenda:
        print("\n❌ ...No hay Contactos en la Agenda... ❌")
    else:
        nombre = input("\nNombre del contacto a Modificar: ").upper().strip()
        if nombre in agenda:
            print(f"\n{'Nombre':<15}{'Teléfono':<15}{'Email':<15}")
            print(f"-" * 60)
            print(f"{nombre:<15}{agenda[nombre][0]:<15}{agenda[nombre][1]:<15}")
            print(f"-" * 60)
            resp = input("¿Deseas modificar el contacto? (Si/No): ").upper().strip()
            if resp == "SI":
                telefono = input("\nTeléfono: ").strip()
                email = input("Email: ").upper().strip()
                agenda[nombre] = [telefono, email]
                print("\n✅ :: Acción realizada con éxito :: ✅")
        else:
            print("\n❌ ...No existe el contacto... ❌")

def eliminarContacto(agenda):
    borrarPantalla()
    print("📛.:: Modificar Contacto ::.📛")
    if not agenda:
        print("\n❌ ...No hay Contactos en la Agenda... ❌")
    else:
        nombre = input("\nNombre del contacto a buscar: ").upper().strip()
        if nombre in agenda:
            print(f"\n{'Nombre':<15}{'Teléfono':<15}{'Email':<15}")
            print(f"-" * 60)
            print(f"{nombre:<15}{agenda[nombre][0]:<15}{agenda[nombre][1]:<15}")
            print(f"-" * 60)
            resp = input("¿Deseas eliminar el contacto? (Si/No): ").upper().strip()
            if resp == "SI":
                agenda.pop(nombre)
                print("\n✅ :: Acción realizada con éxito :: ✅")
        else:
            print("\n❌ ...No existe el contacto... ❌")

