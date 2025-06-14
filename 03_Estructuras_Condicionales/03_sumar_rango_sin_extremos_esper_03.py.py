#Programa que permita solo ingresar numeros enteros
#Si el usuario no puso numero par, volver a pedir que ingrese un numero entero

#Solicitamos al usuario ingrese un numero.
nUmerO=int(input("Ingrese un numero par: "))

#Programa principal que verifica si el numero ingresa es par o impar.
if nUmerO % 2 == 0: 
        print("El numero ingresado es un numero entero")
else:
        print("El numero ingresado no es un numero entero, vuelva a ingresar un numero entero")
