#Definimos funcion. 
def calcular_promedio(a, b, c):
    return (a + b + c) / 3  # Sumamos los 3 valores y dividimos por 3

# Programa principal
a = float(input("Primer número: ")) # Pedimos el primer número como decimal
b = float(input("Segundo número: "))  # Pedimos el segundo número
c = float(input("Tercer número: ")) # Pedimos el tercer número

promedio = calcular_promedio(a, b, c) #Llamamos a la funcion para calcular el promedio.
print(f"El promedio es: {promedio:.2f}") # Mostramos el resultado con 2 decimales
