#Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un número entero positivo indicado por el usuario.


num = int(input("Ingrese un número entero positivo: ")) # Solicitamos al usuario ingrese un numero que sea positivo.
suma = 0  # Incializamos la variable suma en 0.

for i in range(num + 1):  # Iteramos desde 0 hasta num
    suma += i  # Acumulamos la suma

print("La suma de los números entre 0 y", num, "es:", suma) 