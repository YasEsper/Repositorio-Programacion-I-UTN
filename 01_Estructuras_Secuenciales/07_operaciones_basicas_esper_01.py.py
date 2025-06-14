#Definimos variables 
num_1 = int(input("Por favor, ingrese el primer número: ")) # solicitamos al usuario, ingrese un numero 
num_2 = int(input("Por favor, ingrese el segundo número: "))# solicitamos al usuario, ingrese un numero 

# Realizamos operaciones.
suma = num_1 + num_2 
resta = num_1 - num_2
multiplicacion = num_1 * num_2
division = num_1 / num_2

#Imprimimos respuestas en pantalla.
print(f"Suma: {suma}")
print(f"Resta: {resta}")
print(f"Multiplicación: {multiplicacion}")
print(f"División: {division:.2f}") 
