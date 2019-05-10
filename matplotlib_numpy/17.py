from matplotlib import pyplot as plt
import numpy as np
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import sympy
import sys


figure1 = plt.figure()
ax = Axes3D(figure1)
X = np.arange(0, np.pi, 0.25)
Y = np.arange(0, np.pi*2, 0.25)
X, Y = np.meshgrid(X, Y)
Z = np.sqrt(15/(4*np.pi))*np.sin(X)*np.cos(X)*np.cos(Y)
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='rainbow')



plt.show()