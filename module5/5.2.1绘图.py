
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 1)
y = np.sin(4 * np.pi * x) * np.exp(-5 * x)
plt.plot(x, y,'r--')
plt.xlabel("x")
plt.ylabel("y")
plt.title("111")
plt.show()