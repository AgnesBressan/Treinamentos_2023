#exercicio 5 treinamento semear python
# Thiago Goncalves

import numpy as np
import matplotlib.pyplot as plt

i = -50
f = 50
n = 1000

x = np.linspace(i, f, n)
ale = np.random.randint(i, f, n)

y = ale * x**2

plt.title('gráfico a partir de números aleatórios')
plt.xlabel('eixo x')
plt.ylabel('funcao')
plt.grid(True)
plt.plot(x, y, label = 'funcao')
plt.legend()
plt.show()



