#Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule lamedia de esos valores. 

suma = 0  
contador = 0  

while contador < 100:  # Repetimos hasta llegar a 100 números ingresados
    numero = int(input(f"Ingrese el número {contador + 1}: "))  # Solicitamos un numero al usuario.
    suma += numero  # Sumamos el número ingresado
    contador += 1  # Incrementamos el contador

media = suma / 100  # Calculamos el promedio

print("La media de los 100 números ingresados es:", media)  # Mostramos el resultadoS