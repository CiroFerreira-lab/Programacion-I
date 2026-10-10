# Alumno: Ciro Ferreira
# Materia: Programación I
# Actividad 01

nombres_jugadores = []
categorias_jugadores = []

nombres_parejas = []
jugador1_parejas = []
jugador2_parejas = []

cantidad_jugadores = int(input("¿Cuántos jugadores van a participar en el torneo?: "))

while cantidad_jugadores % 2 != 0 or cantidad_jugadores <= 0:
    print("Error: La cantidad de jugadores debe ser un número par.")
    cantidad_jugadores = int(input("¿Cuántos jugadores van a participar en el torneo?: "))

for i in range(cantidad_jugadores):
    print()
    print(f"Datos del Jugador {i + 1}:")
    nombre = input("Nombre del jugador: ")
    categoria = input("Categoría (ej. 4ta, 5ta, 6ta): ")
    
    nombres_jugadores.append(nombre)
    categorias_jugadores.append(categoria)

print()
print("--- Armado de parejas ---")
print("Jugadores inscriptos para elegir:")

for i in range(cantidad_jugadores):
    print(f"- {nombres_jugadores[i]} (Categoría: {categorias_jugadores[i]})")

cantidad_parejas = cantidad_jugadores // 2

for i in range(cantidad_parejas):
    print()
    print(f"Armando Pareja {i + 1}:")
    nombre_pareja = input("Nombre de la pareja (ej. Los Tanos): ")
    jugador1 = input("Nombre del Jugador 1: ")
    jugador2 = input("Nombre del Jugador 2: ")
    
    nombres_parejas.append(nombre_pareja)
    jugador1_parejas.append(jugador1)
    jugador2_parejas.append(jugador2)

print()
print("Resumen de las parejas formadas:")
for i in range(cantidad_parejas):
    print(f"Pareja '{nombres_parejas[i]}': {jugador1_parejas[i]} y {jugador2_parejas[i]}")


