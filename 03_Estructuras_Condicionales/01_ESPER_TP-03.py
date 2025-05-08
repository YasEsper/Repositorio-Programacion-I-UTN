# Escribir un progema que solicite la edad al usuario 
# Luego de eso, evalue si el usuario es mayor de edad

#Solicitamos al usuario ingrese su edad.
Edad_Usuario=input("Por favor, ingrese su edad: ")

Edad_Usuario=int(Edad_Usuario) # convertimos la edad en cadena en un numero entero.
MAYOR_DE_EDAD=18

#Programa principal que evalua edad.
if (Edad_Usuario > MAYOR_DE_EDAD) or (Edad_Usuario == MAYOR_DE_EDAD):
    print("El usuario es mayor de edad")
else:
    print("El usuario es menor de edad")