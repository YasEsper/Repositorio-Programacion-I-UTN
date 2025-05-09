#Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9.
# Al final, el programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

import random  # Importamos la biblioteca para generar números aleatorios

 # Generamos un número aleatorio entre 0 y 9.
numero_secreto = random.randint(0, 9) 

intento = -1  # Inicializamos con un valor diferente a cualquier posible número
intentos = 0  # Contador de intentos

print("¡Bienvenido/a al juego de adivinanza!")
print("Debes adivinar un número entre 0 y 9.")

 # El bucle sigue hasta que el usuario acierte el numero a adivinar.
while intento != numero_secreto: 
    intento = int(input("Ingresa tu número: "))  # Pedimos al usuario que ingrese un número
    intentos += 1  # Contamos el intento

print(f"¡Felicidades! Adivinaste el número en {intentos} intentos.")  