#Definimos variables 
segundos = int(input("Por favor, ingrese la cantidad de segundos: ")) #Solicitamos ingrese segundos,tranformamos cadena en entero.
horas = segundos / 3600 # Calculamos horas.
#Mostramos en pantalla a cuantas horas equivalen los segundos ingresados.
print(f"{segundos} segundos equivalen a {horas:.2f} horas") 