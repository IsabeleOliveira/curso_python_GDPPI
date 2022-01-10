from collections import deque
from time import sleep


# Estrutura de Fila

"""
fila = deque()
fila.append('Isabele')
fila.append('Lucas')
fila.append('Davi')
fila.append('Gabriel')

fila.popleft()

for nome in fila:
    print(nome)

"""


fila = deque(maxlen=10)

for i in range(10):
    fila.append(i)
    sleep(1)
    print(fila)

