import numpy as np
import matplotlib.pyplot as plt

x = np.random.randint(0, 100, 100)
y = np.random.randint(0, 100, 100)
#y = np.arange(0, 100, 1)

plt.scatter(x, y, color="purple")
plt.grid()
plt.title("Aleatórios")
plt.xlabel("eixo x")
plt.ylabel("eixo y")
plt.legend("???")
plt.show()
