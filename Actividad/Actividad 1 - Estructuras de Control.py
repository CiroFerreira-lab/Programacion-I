# Alumno: Ciro Ferreira
# Materia: Programación I
# Actividad 01

mensaje = input("Ingresá el mensaje a codificar: ")

# Convertimos todo a mayúsculas
mensaje_mayus = mensaje.upper()

# Quitamos los acentos reemplazándolos por la letra normal
mensaje_sin_acentos = mensaje_mayus.replace("Á", "A")
mensaje_sin_acentos = mensaje_sin_acentos.replace("É", "E")
mensaje_sin_acentos = mensaje_sin_acentos.replace("Í", "I")
mensaje_sin_acentos = mensaje_sin_acentos.replace("Ó", "O")
mensaje_sin_acentos = mensaje_sin_acentos.replace("Ú", "U")

# Reemplazamos las vocales por los códigos de los espías
mensaje_codificado = mensaje_sin_acentos.replace("A", "X")
mensaje_codificado = mensaje_codificado.replace("E", "W")
mensaje_codificado = mensaje_codificado.replace("I", "K")
mensaje_codificado = mensaje_codificado.replace("O", "&")
mensaje_codificado = mensaje_codificado.replace("U", "%")

print()
print("Mensaje codificado:")
print(mensaje_codificado)