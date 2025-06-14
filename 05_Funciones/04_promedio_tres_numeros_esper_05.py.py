import math #Importamos la librerira de math para usar el valor de Pi

def calcular_area_circulo(radio): #Definimos funcion para calcular area del circulo.
    return math.pi * radio ** 2 # Fórmula: π × radio²(area)

def calcular_perimetro_circulo(radio): #Definimos funcion para calcular el perimetro 
    return 2 * math.pi * radio # Fórmula: 2 × π × radio(perimetro)

#Programa principal 
radio = float(input("Ingresá el radio del círculo: "))
print("Área:", calcular_area_circulo(radio))        # Usamos un print para mostrar en la pantalla el area llamando a la funcion.
print("Perímetro:", calcular_perimetro_circulo(radio))  # Usamos un print para mostrar en la pantalla el perimetro llamando a la funcion.
