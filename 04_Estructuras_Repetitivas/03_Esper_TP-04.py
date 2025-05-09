#Escribe un programa que sume todos los números enteros comprendidos entre dos valores dados por el usuario, excluyendo esos dos valores.

# Solicitar al usuario dos números
num1 = int(input("Por favor, ingrese un numero: "))
num2 = int(input("Por favor, ingrese otro numero: "))

# Necesitamos que el numero menor se al primero.
inicio = min(num1, num2) + 1  # Excluyendo el menor
fin = max(num1, num2)  # Excluyendo el mayor

suma = 0 # Inicializamos suma en 0.

for i in range(inicio, fin):
    suma += i  # Acumula la suma

print("La suma de los números entre", num1, "y", num2, "excluyendo ambos, es:", suma)