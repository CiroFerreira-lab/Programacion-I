import os

def mostrar_menu():
    print("\n--- MENU BUFFET ---")
    print("1. Registrar venta")
    print("2. Ver informes de la semana")
    print("3. Guardar y salir")

def main():
    codigos = []
    nombres = []
    precios = []
    cantidades_vendidas = []
    
    datos_nuevos = [
        [101, "Cafe", 1500],
        [102, "Medialuna", 700],
        [103, "Alfajor", 1000]
    ]

    for producto in datos_nuevos:
        cod = producto[0]
        repetido = False
        for c in codigos:
            if c == cod:
                repetido = True
        
        if repetido == False:
            codigos.append(cod)
            nombres.append(producto[1])
            precios.append(producto[2])
            cantidades_vendidas.append(0)
            
    recaudacion_dias = [0.0, 0.0, 0.0, 0.0, 0.0] 

    if os.path.exists("ventas_buffet.txt"):
        archivo = open("ventas_buffet.txt", "r")
        for i in range(len(codigos)):
            cantidades_vendidas[i] = int(archivo.readline())
        for i in range(5):
            recaudacion_dias[i] = float(archivo.readline())
        archivo.close()

    opcion = 0
    while opcion != 3:
        mostrar_menu()
        opcion = int(input("Elegí una opción: "))

        if opcion == 1:
            dia = int(input("Día (1 Lunes - 5 Viernes): "))
            cod = int(input("Código del producto: "))
            cant = int(input("Cantidad vendida: "))

            indice = -1
            for i in range(len(codigos)):
                if codigos[i] == cod:
                    indice = i
            
            if indice != -1 and (dia >= 1 and dia <= 5):
                cantidades_vendidas[indice] = cantidades_vendidas[indice] + cant
                recaudacion_dias[dia - 1] = recaudacion_dias[dia - 1] + (cant * precios[indice])
                print("Venta registrada.")
            else:
                print("Error: Datos incorrectos.")

        elif opcion == 2:
            print("\n--- INFORMES ---")
            total_semana = 0
            print("Unidades vendidas:")
            for i in range(len(codigos)):
                print(f"- {nombres[i]}: {cantidades_vendidas[i]}")
            
            print("\nRecaudación por día:")
            for i in range(5):
                print(f"- Día {i+1}: ${recaudacion_dias[i]}")
                total_semana = total_semana + recaudacion_dias[i]
            
            print(f"\nRecaudación TOTAL: ${total_semana}")

        elif opcion == 3:
            archivo = open("ventas_buffet.txt", "w")
            for i in range(len(codigos)):
                archivo.write(str(cantidades_vendidas[i]) + "\n")
            for i in range(5):
                archivo.write(str(recaudacion_dias[i]) + "\n")
            archivo.close()
            print("Guardando y saliendo...")
        else:
            print("Opción inválida.")

main()