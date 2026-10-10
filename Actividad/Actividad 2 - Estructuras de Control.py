# Alumno: Ciro Ferreira
# Materia: Programación I
# Actividad 02

parrafo = input("Ingresá el párrafo del ensayo: ")

# El split() sin parámetros separa por espacios en blanco
palabras = parrafo.split()

cantidad = len(palabras)

print()
print(f"Resultado correcto: {cantidad}")