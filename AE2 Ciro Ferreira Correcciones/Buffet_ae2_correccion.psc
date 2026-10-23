Algoritmo Buffet_AE2
    Definir codigos, precios, cantidades, dia, cod, cant, i, opc, indice Como Entero
    Definir nombres Como Cadena
    Definir recaudacion_dias, total_semana Como Real
	
    Dimension codigos[6], nombres[6], precios[6], cantidades[6], recaudacion_dias[5]
	
    codigos[1] <- 101; nombres[1] <- "Cafe con leche"; precios[1] <- 1500; cantidades[1] <- 0
    codigos[2] <- 102; nombres[2] <- "Medialuna"; precios[2] <- 700; cantidades[2] <- 0
    codigos[3] <- 103; nombres[3] <- "Sandwich de miga"; precios[3] <- 1800; cantidades[3] <- 0
    codigos[4] <- 104; nombres[4] <- "Agua mineral 500 ml"; precios[4] <- 1000; cantidades[4] <- 0
    codigos[5] <- 105; nombres[5] <- "Empanada"; precios[5] <- 1200; cantidades[5] <- 0
    codigos[6] <- 106; nombres[6] <- "Chipa (100 g)"; precios[6] <- 1300; cantidades[6] <- 0

    Para i <- 1 Hasta 5 Con Paso 1 Hacer
        recaudacion_dias[i] <- 0
    FinPara
	
    opc <- 0
    Mientras opc <> 3 Hacer
        Escribir "1. Registrar venta | 2. Ver informes | 3. Guardar y salir"
        Leer opc
		
        Segun opc Hacer
            1:
                Escribir "Dia (1 a 5): "; Leer dia
                Escribir "Codigo: "; Leer cod
                Escribir "Cantidad: "; Leer cant
				
                indice <- 0
                Para i <- 1 Hasta 6 Con Paso 1 Hacer
                    Si codigos[i] = cod Entonces
                        indice <- i
                    FinSi
                FinPara
				
                Si indice > 0 Y dia >= 1 Y dia <= 5 Y cant > 0 Entonces
                    cantidades[indice] <- cantidades[indice] + cant
                    recaudacion_dias[dia] <- recaudacion_dias[dia] + (cant * precios[indice])
                    Escribir "Venta guardada."
                Sino
                    Escribir "Error de datos."
                FinSi
            2:
                total_semana <- 0
                Para i <- 1 Hasta 6 Con Paso 1 Hacer
                    Escribir nombres[i], ": ", cantidades[i]
                FinPara
                Para i <- 1 Hasta 5 Con Paso 1 Hacer
                    Escribir "Dia ", i, ": $", recaudacion_dias[i]
                    total_semana <- total_semana + recaudacion_dias[i]
                FinPara
                Escribir "Total: $", total_semana
            3:
                Escribir "Guardando y saliendo..."
        FinSegun
    FinMientras
FinAlgoritmo