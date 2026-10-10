Algoritmo Buffet_AE2
    Definir codigos, precios, cantidades, dia, cod, cant, i, opc, indice Como Entero
    Definir nombres Como Cadena
    Definir recaudacion_dias Como Real
    
    Dimension codigos[3], nombres[3], precios[3], cantidades[3], recaudacion_dias[5]
    
    codigos[1] <- 101; nombres[1] <- "Cafe"; precios[1] <- 1500; cantidades[1] <- 0
    codigos[2] <- 102; nombres[2] <- "Medialuna"; precios[2] <- 700; cantidades[2] <- 0
    codigos[3] <- 103; nombres[3] <- "Alfajor"; precios[3] <- 1000; cantidades[3] <- 0
    
    Para i <- 1 Hasta 5 Con Paso 1 Hacer
        recaudacion_dias[i] <- 0
    FinPara
    
    opc <- 0
    Mientras opc <> 3 Hacer
        Escribir "1. Registrar venta | 2. Ver informes | 3. Salir"
        Leer opc
        
        Segun opc Hacer
            1:
                Escribir "Dia (1 a 5): "; Leer dia
                Escribir "Codigo: "; Leer cod
                Escribir "Cantidad: "; Leer cant
                
                indice <- 0
                Para i <- 1 Hasta 3 Con Paso 1 Hacer
                    Si codigos[i] = cod Entonces
                        indice <- i
                    FinSi
                FinPara
                
                Si indice > 0 Y dia >= 1 Y dia <= 5 Entonces
                    cantidades[indice] <- cantidades[indice] + cant
                    recaudacion_dias[dia] <- recaudacion_dias[dia] + (cant * precios[indice])
                    Escribir "Venta guardada."
                Sino
                    Escribir "Error de datos."
                FinSi
            2:
                Escribir "Informes..."
            3:
                Escribir "Guardando..."
        FinSegun
    FinMientras
FinAlgoritmo
