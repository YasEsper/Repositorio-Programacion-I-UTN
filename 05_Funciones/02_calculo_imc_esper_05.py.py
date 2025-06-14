# Definimos funcion, le damos un parametro llamado nombre
def saludar_usuario(nombre): 
    return f"Hola {nombre}!"

# Programa principal
nombre_ingresado = input("Ingresá tu nombre: ")# Pedimos al usuario que ingrese su nombre y lko guardamos en una variable.
print(saludar_usuario(nombre_ingresado))#Lamamos a la funcion pasandole el nombre ingresado y mostramos el saludo.
