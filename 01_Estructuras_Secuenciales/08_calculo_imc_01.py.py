#definbimos variables.
altura = float(input("Por favor, ingrese su altura en metros: ")) #Solicitamos al usuario altura.
peso = float(input("Por favor, ingrese su peso en kg: "))#Solicitamso al usuario peso.
imc = peso / (altura ** 2) # Calculamos ICM

#Imprimimos en pantalla.
print(f"Su índice de masa corporal es: {imc:.2f}") 