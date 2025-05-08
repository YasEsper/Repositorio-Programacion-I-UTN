#Se solicita al usuario ingrese la nota 
#Una ves realizado, se evalua si la nota es mayor a 6 
#Se imprime un carten en pantalla que muestra si aprobo o no

#Solicitamos nota al usuario 
Nota=int(input("Por favor, ingrese la nota que se saco: "))
NOTA_APROBACION= 6

#Programa principal que evalua si aprobo o no.
if (Nota > 6) or (Nota == 6):
        print("Aprobado")
else:
        print("Desaprobado")