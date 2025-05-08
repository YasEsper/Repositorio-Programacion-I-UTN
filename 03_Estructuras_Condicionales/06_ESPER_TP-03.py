#Un programa que tome una lista aleatoria y calcule moda mediana y media.
#Y que con esos datos compare y determine si es sesgo posituvi, negativo o no hay sesgo

import random
from statistics import mode, median, mean

# Generamos una lista de 50 numeros aleatorios entre el 1 y el 100
numeros_aleatorios = [random.randint(1, 100) for _ in range(50)]

# Solicitamos calcule la moda mediana y media.
moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)

# Programa principal donde se verifica el sesgo.
if media > mediana > moda:
    sesgo = "Sesgo positivo (derecha)"
elif media < mediana < moda:
    sesgo = "Sesgo negativo (izquierda)"
else:
    sesgo = "Sin sesgo"

# Imprimimos resultados. 
print(f"Números aleatorios: {numeros_aleatorios}")
print(f"Moda: {moda}")
print(f"Mediana: {mediana}")
print(f"Media: {media}")
print(f"Distribución: {sesgo}")