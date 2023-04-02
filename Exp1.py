import matplotlib.piplot as plt
import numpy as np

x = np.linspace(0, 2 * np.p1, 200)
y = np.sin(x)

fig, ax = plt.subplots()
ax.plot(x,y)
plt.show()