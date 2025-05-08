#Escribir un programa que solicite intruducir una contraseña.
#Luego, evalue si el usuario introdusco.

#Solicitamos al usuario ingrese una contraseña de etre 8 y 14 caracteras
contraseña=input("Por favor, ingrese una contraseña entre 8 y 14 caracteres: ")

#Programa donde evalua si la contraseña tiene esa cantidad de caracteres.
if 8 <= len(contraseña) < 14:
        print("Ha ingresado una contraseña correcta")
else:
        print("Por favor, ingrese una contraseña que contenga entre 8 y 14 caracteres") #Si no contiene, se solicita vuelva a ingresar la contraseña.