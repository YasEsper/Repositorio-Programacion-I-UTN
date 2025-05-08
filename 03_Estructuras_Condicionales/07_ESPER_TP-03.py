#Programa que solicita al usuario ingrese una palabra o frase.
#Si el string termina en vocal se soliciata al progra imprima con !

# Solicitar una frase o palabra al usuario.
texto = input("Ingresa una frase o palabra: ")

# Verificar si la última letra es una vocal.
if texto[-1] in ("a", "e", "i", "o", "u", "A", "E", "I", "O", "U"):
    texto += "!"

# Imprimir el resultado.
print(texto)