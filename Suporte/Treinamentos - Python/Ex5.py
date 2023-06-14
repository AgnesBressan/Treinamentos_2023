"""
Exercicio 5 - Treinamento Python NRA SEMEAR
Marco Soprani Tayar (Suporte)
"""

import numpy as np
import matplotlib.pyplot as mp

x = []
for i in range(20):
    x.append(i)
y = np.random.randint(0, 1000, 20)

mp.title('Gráfico aleatório')
mp.xlabel('Posição')
mp.ylabel('Valores')
mp.grid(True)
mp.plot(x, y, label='teste')
mp.legend()
mp.show()
