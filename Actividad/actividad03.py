import json

ARCHIVO_INSCRIPTOS = "inscriptos.json"
ARCHIVO_PAREJAS = "parejas.json"


def cargar(nombre_archivo):
    try:
        archivo = open(nombre_archivo, "r", encoding="utf-8")
        datos = json.load(archivo)
        archivo.close()
        return datos
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def guardar(nombre_archivo, datos):
    archivo = open(nombre_archivo, "w", encoding="utf-8")
    json.dump(datos, archivo, ensure_ascii=False, indent=4)
    archivo.close()


def clave_nombre(jugador):
    return jugador["nombre"].lower()


def clave_categoria_nombre(jugador):
    return (jugador["categoria"], jugador["nombre"].lower())


def clave_puntos(pareja):
    return pareja["puntos"]


def seleccion(lista, clave, descendente=False):
    datos = lista[:]
    comparaciones = 0
    intercambios = 0
    n = len(datos)

    for i in range(n - 1):
        pos = i
        for j in range(i + 1, n):
            comparaciones += 1
            if descendente:
                if clave(datos[j]) > clave(datos[pos]):
                    pos = j
            else:
                if clave(datos[j]) < clave(datos[pos]):
                    pos = j
        if pos != i:
            auxiliar = datos[i]
            datos[i] = datos[pos]
            datos[pos] = auxiliar
            intercambios += 1

    return datos, comparaciones, intercambios


def burbuja(lista, clave, descendente=False):
    datos = lista[:]
    comparaciones = 0
    intercambios = 0
    n = len(datos)

    for i in range(n - 1):
        hubo_cambio = False
        for j in range(n - 1 - i):
            comparaciones += 1
            if descendente:
                fuera_de_orden = clave(datos[j]) < clave(datos[j + 1])
            else:
                fuera_de_orden = clave(datos[j]) > clave(datos[j + 1])
            if fuera_de_orden:
                auxiliar = datos[j]
                datos[j] = datos[j + 1]
                datos[j + 1] = auxiliar
                intercambios += 1
                hubo_cambio = True
        if not hubo_cambio:
            break

    return datos, comparaciones, intercambios


opcion = "-1"

while opcion != "0":
    print()
    print("SISTEMA DE GESTIÓN - ARCHIVOS")
    print("1. Inscribir un nuevo jugador")
    print("2. Mostrar lista completa de inscriptos")
    print("3. Buscar si un jugador está inscripto")
    print("4. Dar de baja a un jugador lesionado")
    print("5. Lista alfabética (Selección)")
    print("6. Lista por categoría (Burbuja)")
    print("7. Crear pareja")
    print("8. Cargar puntos a una pareja")
    print("9. Tabla de posiciones")
    print("10. Comparar métodos")
    print("0. Salir")

    opcion = input("Elegí una opción: ")

    if opcion == "1":
        print()
        inscriptos = cargar(ARCHIVO_INSCRIPTOS)
        nombre = input("Nombre del jugador: ").strip()
        categoria = input("Categoría (ej. 4ta, 5ta, 6ta): ").strip()

        repetido = False
        for jugador in inscriptos:
            if jugador["nombre"].lower() == nombre.lower():
                repetido = True

        if nombre == "":
            print("El nombre no puede estar vacío.")
        elif repetido:
            print(f"El jugador {nombre} ya está inscripto.")
        else:
            inscriptos.append({"nombre": nombre, "categoria": categoria})
            guardar(ARCHIVO_INSCRIPTOS, inscriptos)
            print(f"El jugador {nombre} fue guardado correctamente.")

    elif opcion == "2":
        print()
        inscriptos = cargar(ARCHIVO_INSCRIPTOS)
        if len(inscriptos) == 0:
            print("La lista está vacía.")
        else:
            for jugador in inscriptos:
                print(f"- Jugador: {jugador['nombre']} | Categoría: {jugador['categoria']}")

    elif opcion == "3":
        print()
        inscriptos = cargar(ARCHIVO_INSCRIPTOS)
        nombre_buscar = input("Ingresá el nombre del jugador a buscar: ")
        encontrado = False

        for jugador in inscriptos:
            if jugador["nombre"].lower() == nombre_buscar.lower():
                print(f"Encontrado: {jugador['nombre']} juega en {jugador['categoria']}.")
                encontrado = True
                break

        if not encontrado:
            print(f"El jugador '{nombre_buscar}' no está inscripto.")

    elif opcion == "4":
        print()
        inscriptos = cargar(ARCHIVO_INSCRIPTOS)
        nombre_baja = input("Ingresá el nombre del jugador a dar de baja: ")
        encontrado = False

        for i in range(len(inscriptos)):
            if inscriptos[i]["nombre"].lower() == nombre_baja.lower():
                inscriptos.pop(i)
                encontrado = True
                break

        if encontrado:
            guardar(ARCHIVO_INSCRIPTOS, inscriptos)
            print(f"El jugador {nombre_baja} fue eliminado.")
        else:
            print(f"No se encontró a '{nombre_baja}'.")

    elif opcion == "5":
        print()
        inscriptos = cargar(ARCHIVO_INSCRIPTOS)
        if len(inscriptos) == 0:
            print("La lista está vacía.")
        else:
            ordenada, comp, interc = seleccion(inscriptos, clave_nombre)
            print("Inscriptos en orden alfabético:")
            for jugador in ordenada:
                print(f"- {jugador['nombre']}")

    elif opcion == "6":
        print()
        inscriptos = cargar(ARCHIVO_INSCRIPTOS)
        if len(inscriptos) == 0:
            print("La lista está vacía.")
        else:
            ordenada, comp, interc = burbuja(inscriptos, clave_categoria_nombre)
            categoria_actual = ""
            for jugador in ordenada:
                if jugador["categoria"] != categoria_actual:
                    categoria_actual = jugador["categoria"]
                    print(f"Categoría {categoria_actual}:")
                print(f"   - {jugador['nombre']}")

    elif opcion == "7":
        print()
        parejas = cargar(ARCHIVO_PAREJAS)
        nombre_pareja = input("Nombre de la pareja: ").strip()
        jugador1 = input("Jugador 1: ").strip()
        jugador2 = input("Jugador 2: ").strip()

        repetida = False
        for pareja in parejas:
            if pareja["nombre"].lower() == nombre_pareja.lower():
                repetida = True

        if nombre_pareja == "":
            print("El nombre no puede estar vacío.")
        elif repetida:
            print("Ya existe una pareja con ese nombre.")
        else:
            parejas.append({"nombre": nombre_pareja,
                            "jugadores": [jugador1, jugador2],
                            "puntos": 0})
            guardar(ARCHIVO_PAREJAS, parejas)
            print(f"La pareja {nombre_pareja} fue guardada.")

    elif opcion == "8":
        print()
        parejas = cargar(ARCHIVO_PAREJAS)
        nombre_pareja = input("¿A qué pareja le cargás puntos? ").strip()
        encontrada = False

        for pareja in parejas:
            if pareja["nombre"].lower() == nombre_pareja.lower():
                encontrada = True
                try:
                    puntos = int(input("Puntos a sumar: "))
                    pareja["puntos"] += puntos
                    guardar(ARCHIVO_PAREJAS, parejas)
                    print("Puntos cargados.")
                except ValueError:
                    print("Tenés que ingresar un número entero.")
                break

        if not encontrada:
            print("No existe esa pareja.")

    elif opcion == "9":
        print()
        parejas = cargar(ARCHIVO_PAREJAS)
        if len(parejas) == 0:
            print("Todavía no hay parejas cargadas.")
        else:
            ordenada, comp, interc = seleccion(parejas, clave_puntos, True)
            print("Puesto | Pareja          | Puntos")
            puesto = 1
            for pareja in ordenada:
                print(f"{puesto:<6} | {pareja['nombre']:<15} | {pareja['puntos']}")
                puesto += 1

    elif opcion == "10":
        print()
        inscriptos = cargar(ARCHIVO_INSCRIPTOS)
        if len(inscriptos) < 2:
            print("Hacen falta al menos 2 jugadores para comparar.")
        else:
            lista1, comp1, interc1 = seleccion(inscriptos, clave_nombre)
            lista2, comp2, interc2 = burbuja(inscriptos, clave_categoria_nombre)
            print(f"{'Pedido':<22}{'Método':<12}{'Comparaciones':<15}Intercambios")
            print(f"{'1. Orden alfabético':<22}{'Selección':<12}{comp1:<15}{interc1}")
            print(f"{'2. Por categoría':<22}{'Burbuja':<12}{comp2:<15}{interc2}")

    elif opcion == "0":
        print("Cerrando el sistema...")

    else:
        print("Opción incorrecta.")