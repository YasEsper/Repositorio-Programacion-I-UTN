#Escribe un programa que invierta el orden de los dígitos de un número ingresado por el usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

#Pedimos al usuario un numero, este lo dejamos en cadena.
numero = input("Ingrese un número: ")  
numero_invertido = numero[::-1]  # Invertimos el orden de los dígitos
print("El número invertido es:", numero_invertido)  # Mostramos el resultado