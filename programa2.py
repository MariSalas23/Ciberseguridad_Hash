# Carlos Augusto Sanchez Lombana y Mariana Salas Gutiérrez

#PROGRAMA 2

# Librerías
import hashlib
import random
import time

# Listas
lista = [0] * 50
hashes = []

for i in range(50):
    numero = random.randint(1, 100_000_000)
    lista[i] = numero
    # Código de referencia: user_hash = hashlib.sha256(texto.encode()).hexdigest()
    h = hashlib.sha256(str(numero).encode()).hexdigest()
    hashes.append(h)

# Inicia cronómetro
inicio = time.time()

# Comparar con todos los hashes de 1 a 100 000 000
for j in range(1, 100_000_001):
    j_hash = hashlib.sha256(str(j).encode()).hexdigest()
    if j_hash in hashes:
        print(j, j_hash)

# Finaliza cronómetro
fin = time.time()  
print("Tiempo total:", round(fin - inicio, 2), "segundos")