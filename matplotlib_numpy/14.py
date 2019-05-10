from matplotlib import pyplot as plt
import numpy as np
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import sympy
import sys
# R = 10
# X = np.arange(0, np.pi*2, 0.25)
# Y = np.arange(0, np.pi*2, 0.25)
# #网格化数据
# X, Y = np.meshgrid(X, Y)
#
# R = np.sqrt(3/(4*np.pi))
# Z = R*np.cos(X)
'''
R为P点与原点的距离 X,Y为方位角 
'''
# A = 2
# B = 2
# R = 10
# X = np.arange(0, np.pi, 0.25)
# Y = np.arange(0, np.pi*2, 0.25)
# X, Y = np.meshgrid(X, Y)  # 网格化数据

# m = np.random(1, 10, 1)
M = (2**np.e)*np.math.factorial(2)
u = sympy.Symbol('u')
P = 1/M*(u**2-1)**np.e
p(u) = sympy.diff(P, u, 2)
print(P(u))
# P(m) = (1-u**2)**(m/2)*sympy.diff(p(u),u,m)
# print(P(m))
# P(1) = (-1)**m*np.sqrt([(2*np.e+1)/(4*np.pi)]*[np.math.factorial(np.e-m)/np.math.factorial(np.e+m)])*p(m)
# print(P(1))

#
# figure3 = plt.figure()
#
# ax = Axes3D(figure3)
# Z1 = A*R*np.exp(-B*R/2)*np.sqrt(3/(4*np.pi))*np.sin(X)*np.cos(Y)
# ax.plot_surface(X, Y, Z1, rstride=1, cstride=1, cmap='rainbow')


# figure1 = plt.figure()
# ax = Axes3D(figure1)
# Z2 = A*R*np.exp(-B*R/2)*np.sqrt(3/(4*np.pi))*np.cos(X)
# ax.plot_surface(X, Y, Z2, rstride=1, cstride=1, cmap='rainbow')

#
# figure2 = plt.figure()
# ax = Axes3D(figure2)
# Z3 = A*R*np.exp(-B*R/2)*np.sqrt(3/(4*np.pi))*np.sin(X)*np.sin(Y)
# ax.plot_surface(X, Y, Z3, rstride=1, cstride=1, cmap='rainbow')


# plt.show()