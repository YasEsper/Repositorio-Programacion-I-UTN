#Definimos variables.
temp_celsius = float(input("Ingrese la temperatura en °C: ")) #Solicitamos al usuario temp en ° celsius.
temp_fahrenheit = (temp_celsius * 9/5) + 32 # Calculo para pasar ° celsius a ° fahrenheit.

#Imprimimos en pantalla resultados.
print(f"La temperatura en Fahrenheit es: {temp_fahrenheit:.2f} °F")