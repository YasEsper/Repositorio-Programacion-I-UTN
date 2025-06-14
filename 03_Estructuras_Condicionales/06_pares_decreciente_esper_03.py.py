#Solicitamos al usuario que ingrese nombre y un numero (1,2 o 3)

# Solicitar el nombre y la opción de formato.
nombre = input("Ingresa tu nombre: ")
opcion = input("Elige una opción (1: mayusculas, 2: minusculas, 3: primera letra en mayuscula): ")

# Aplicar el formato según la opción elegida
if opcion == "1":
    nombre_formateado = nombre.upper()
elif opcion == "2":
    nombre_formateado = nombre.lower()
elif opcion == "3":
    nombre_formateado = nombre.title()
else:
    nombre_formateado = "Opción no válida"

# Mostrar el resultado
print(f"Nombre transformado: {nombre_formateado}") 