#Definimos funciuon para converitr segundos a hora.
def segundos_a_horas(segundos):
    return segundos / 3600  # 1 hora = 3600 segundos.

# Programa principal
segundos = int(input("Ingresá la cantidad de segundos: "))
horas = segundos_a_horas(segundos) #Llamamos a la funcion para pasaer segudnos a hora.
print(f"{segundos} segundos equivalen a {horas:.2f} horas.")  # Mostramos con 2 decimales.