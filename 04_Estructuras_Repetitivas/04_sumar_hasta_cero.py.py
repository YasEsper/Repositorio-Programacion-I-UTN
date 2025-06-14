#Elabora un programa que permita al usuario ingresar números enteros y los sume en secuencia. 
# El programa debe detenerse y mostrar el total acumulado cuando el usuario ingresado sea 0.

suma = 0  # Inicializamos la variable suma en 0.
numero = int(input("Por favor ingrese un número, si desea salir ingrese el numero 0: "))  # Soliciatamos al usuario ingrese un numero entero y aclaramos como salir del bucle.

while numero != 0:  # Mintras el numero ingresado sea distinto de cero se mantiene el bucle.
    suma += numero  # Acumulamos la suma
    numero = int(input("Por favor ingrese un número, si desea salir ingrese el numero 0: "))  # Pedimos otro número

print("La suma total es:", suma)  