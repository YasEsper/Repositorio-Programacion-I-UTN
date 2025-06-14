#definimos funcion para pasar de ° celsius a fahrenheit.
def celsius_a_fahrenheit(celsius):
    return celsius * 9 / 5 + 32  # Calculamso con la fórmula: (C × 9/5) + 32 

# Programa principal
celsius = float(input("Ingresá la temperatura en °C: "))
fahrenheit = celsius_a_fahrenheit(celsius) # Llamamos a la función para convertir y guardamos el resultado

print(f"{celsius} °C equivalen a {fahrenheit:.2f} °F") # Mostramos el resultado formateado con 2 decimales