#Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de dígitos que contiene.

numero = int(input("Por favor, ingrese un numero entero: ")) # Solicitamos al usuario ingrese un numero 

contador = 0 # Inicializamos el contador 

while numero >0 : # Mientras el numero sea mayor a cero.
    numero = numero // 10 #Elimina los digistos diviendo por 10 hasta llegar a 0.
    contador +=1

#Caso especial si el numero igresado es 0, asignamos 1 al contador antes de inciar 
if contador == 0:
    contador = 1

print("El numero tiene ", contador , "digitos. ")
