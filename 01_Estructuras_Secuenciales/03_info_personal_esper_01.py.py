#Definimos variables 
nombre = input("Por favor, ingrese su nombre: ") #Solicitamos al usuario ingrese nombre 
apellido = input("Por favor, ingrese su apellido: ") # Solicitamos al usuario ingrese apellido
edad = int(input("Por favor, ingrese su edad: ")) # solicitamos al usuario ingrese edad y convertimos string en entero.
ciudad = input("Por favor, ingrese su lugar de residencia: ") # Solictamos al usuario ingrese lugar de residencia 

#Mostramos en pantalla frase modificada con los datos solicitados.
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {ciudad}.")  