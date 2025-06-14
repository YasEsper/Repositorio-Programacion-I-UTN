
#Solicite al usuario su edad
#Se imprima en pantalla a  que caterioa pertenece

#Solicitamos al usuario ingrese su edad
Edad=int(input("Por favor ingrese su edad: "))

#Programa principal donde se verifica a que categoria pertene el usuario segun su edad.
if Edad < 12:
    print("Usted pertenece a la categoria Niño/a")
elif Edad >= 12 and Edad < 18:
    print("Usted pertenece a la categoria Adolescente")
elif Edad >= 18 and Edad < 30:
    print("Usted pertenece a la categoria Adulto/a joven")
else:
    print("Usted pertenece a la categoria Adulto/a")
