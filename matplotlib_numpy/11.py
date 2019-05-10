import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt



x = np.arange(-5, 5, 0.01)
y = 3/(8*np.pi)*np.sin(x)**2

plt.plot(x, y)

plt.show()