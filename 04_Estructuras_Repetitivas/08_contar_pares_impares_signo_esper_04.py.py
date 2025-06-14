#Escribe un programa que permita al usuario ingresar 100 números enteros.

suma = 0  # Inicializamos variable suma en 0.
contador = 0  # Incializamos contador en 0.

# Usamos el contador para solicitar numeros al usuario hasta llegar a tener los 100 numeros.
while contador < 100:  
    numero = int(input("Ingrese un número entero: "))  # Solicitamos el número
    suma += numero  # Sumamos el número ingresado
    contador += 1  # Incrementamos el contador

print("La suma total de los 100 números ingresados es:", suma)