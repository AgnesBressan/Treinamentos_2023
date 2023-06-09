import numpy as np
import matplotlib.pyplot as plt

x1 = np.random.randint(1,100,20)
y1 = 2 + x1/2

x2 = np.random.randint(1,100,20)
y2 = x2/4

plt.title('Desempenho do time')
plt.xlabel('Partidas jogadas')
plt.ylabel('Somatória dos gols')
plt.grid(True)

plt.scatter(x1, y1, c='green', label='Partidas em casa')

plt.scatter(x2, y2, c='red', marker='s', label='Partidas fora de casa')

plt.legend(loc='best')
plt.show()
