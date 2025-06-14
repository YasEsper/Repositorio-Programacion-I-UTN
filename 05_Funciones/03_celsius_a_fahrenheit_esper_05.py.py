#Definimos funcion informacion_personal
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.") # Funcion recibe 4 paramentros e imprime en pantalla el mensaje solicitado

# Programa principal
nombre = input("Ingresá tu nombre: ") # Solicitamos al usuario, ingrese su nombre.
apellido = input("Ingresá tu apellido: ") # Solicitamos al usuario ingrese su apellido.
edad = input("Ingresá tu edad: ") # Solicitamos al usuario ingrese su edad.
residencia = input("¿Dónde vivís?: ")# Solicitamos al usuario ingrese el lugar donde vive.

informacion_personal(nombre, apellido, edad, residencia)  # Llamamos a la función con los valores ingresados