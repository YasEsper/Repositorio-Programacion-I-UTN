# Solicitamos al usuario que ingrese en que Hemisferio se encuentra, año y dia.
#El programa imprime en pantalla si esta en otoño, invierno, primavera o verano.

# Solicitar datos al usuario.
hemisferio = input("¿En qué hemisferio te encuentras? (N/S): ").strip().upper()
mes = int(input("Ingresa el número del mes (1-12): "))
dia = int(input("Ingresa el día del mes: "))

# Validar entrada del hemisferio.
if hemisferio not in ["N", "S"]:
    print("Hemisferio no válido. Usa 'N' para Norte o 'S' para Sur.")
    exit()

# Definir las estaciones según los periodos del año.
if (mes == 12 and dia >= 21) or (mes in [1, 2]) or (mes == 3 and dia <= 20):
    estacion = "Invierno" if hemisferio == "N" else "Verano"
elif (mes == 3 and dia >= 21) or (mes in [4, 5]) or (mes == 6 and dia <= 20):
    estacion = "Primavera" if hemisferio == "N" else "Otoño"
elif (mes == 6 and dia >= 21) or (mes in [7, 8]) or (mes == 9 and dia <= 20):
    estacion = "Verano" if hemisferio == "N" else "Invierno"
elif (mes == 9 and dia >= 21) or (mes in [10, 11]) or (mes == 12 and dia <= 20):
    estacion = "Otoño" if hemisferio == "N" else "Primavera"

# Mostrar el resultado
print(f"La estación correspondiente es: {estacion}")