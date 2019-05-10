from numpy import *
import matplotlib as mpl
import matplotlib.pyplot as plt
t = linspace(0, 2 * pi, 50)
x = sin(t)
y = cos(t)
plt.figure()
plt.plot(x)
plt.figure()
plt.plot(y)
plt.show()
