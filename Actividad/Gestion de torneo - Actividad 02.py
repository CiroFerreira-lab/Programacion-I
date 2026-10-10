# Alumno: Ciro Ferreira
# Materia: Programación I
# Actividad 02

NOMBRE_ARCHIVO = "jugadores.txt"
opcion = "0"

while opcion != "5":
    print()
    print("SISTEMA DE GESTIÓN - ARCHIVOS")
    print("1. Inscribir un nuevo jugador")
    print("2. Mostrar lista completa de inscriptos")
    print("3. Buscar si un jugador está inscripto")
    print("4. Dar de baja a un jugador lesionado")
    print("5. Salir")
    
    opcion = input("Elegí una opción: ")

    if opcion == "1":
        print()
        nombre = input("Nombre del jugador: ")
        categoria = input("Categoría (ej. 4ta, 5ta, 6ta): ")
        
        archivo = open(NOMBRE_ARCHIVO, "a")
        archivo.write(f"{nombre},{categoria}\n")
        archivo.close()
        
        print(f"El jugador {nombre} fue guardado correctamente.")

    elif opcion == "2":
        print()
        try:
            archivo = open(NOMBRE_ARCHIVO, "r")
            lineas = archivo.readlines()
            archivo.close()
            
            if len(lineas) == 0:
                print("La lista está vacía.")
            else:
                for linea in lineas:
                    datos = linea.strip().split(",")
                    print(f"- Jugador: {datos[0]} | Categoría: {datos[1]}")
                    
        except FileNotFoundError:
            print("Todavía no se creó el archivo de jugadores.")

    elif opcion == "3":
        print()
        nombre_buscar = input("Ingresá el nombre del jugador a buscar: ")
        encontrado = False
        
        try:
            archivo = open(NOMBRE_ARCHIVO, "r")
            lineas = archivo.readlines()
            archivo.close()
            
            for linea in lineas:
                datos = linea.strip().split(",")
                if datos[0].lower() == nombre_buscar.lower():
                    print(f"Encontrado: {datos[0]} juega en {datos[1]}.")
                    encontrado = True
                    break 
                    
            if not encontrado:
                print(f"El jugador '{nombre_buscar}' no está inscripto.")
                
        except FileNotFoundError:
            print("Todavía no se creó el archivo.")

    elif opcion == "4":
        print()
        nombre_baja = input("Ingresá el nombre del jugador a dar de baja: ")
        
        try:
            archivo = open(NOMBRE_ARCHIVO, "r")
            lineas = archivo.readlines()
            archivo.close()
            
            encontrado = False
            
            archivo = open(NOMBRE_ARCHIVO, "w")
            
            for linea in lineas:
                datos = linea.strip().split(",")
                if datos[0].lower() == nombre_baja.lower():
                    encontrado = True
                else:
                    archivo.write(linea)
            
            archivo.close()
            
            if encontrado:
                print(f"El jugador {nombre_baja} fue eliminado.")
            else:
                print(f"No se encontró a '{nombre_baja}'.")
                
        except FileNotFoundError:
            print("Todavía no se creó el archivo.")

    elif opcion == "5":
        print("Cerrando el sistema...")
        
    else:
        print("Opción incorrecta.")