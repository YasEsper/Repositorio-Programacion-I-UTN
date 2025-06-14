#Definimos funcion para calcular el ICM.
def calcular_imc(peso, altura):
    return round(peso / (altura ** 2), 2)  # Usamos la fórmula del IMC: peso / altura²

# Programa principal
peso = float(input("Ingresá tu peso en kg: "))
altura = float(input("Ingresá tu altura en metros: "))

imc = calcular_imc(peso, altura) #Llamamos a la funcion para calcular el indice de mnasa corporal.
print(f"Tu índice de masa corporal es: {imc}") # Mostramos el IMC calculado