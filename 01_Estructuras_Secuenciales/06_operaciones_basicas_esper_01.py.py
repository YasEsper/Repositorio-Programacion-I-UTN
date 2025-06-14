#Definimos variables
numero = int(input("Por favor, ingrese un número: "))#Solicitamos al usuario ingrese un numero.
print(f"Tabla de multiplicar del {numero}:")#Imprimimos en pantalla tabla de multiplicar.
for i in range(1, 11):# usamos ciclo for para interar del 1 al 10.
    print(f"{numero} x {i} = {numero * i}")