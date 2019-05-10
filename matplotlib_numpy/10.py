from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt
import numpy as np

# 定义基始初量
a = 0.529
A = (1/np.sqrt(np.pi))*a**(-3/2)
B = 1/(4*np.sqrt(2*np.pi*a))
C = (1/(4*np.sqrt(2*np.pi)))*a**(-5/2)
D = (1/(81*np.sqrt(6*np.pi)))*a**(-7/2)

# 定义输出图像函数
def outputimg(X,Y,Z):
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.coolwarm, linewidth=0, antialiased=False)
    ax.set_zlim(-1.01, 1.01)
    ax.zaxis.set_major_locator(LinearLocator(10))
    ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
    fig.colorbar(surf, shrink=0.5, aspect=5)


# 2

X = np.arange(-20, 20, 0.5)
Y = np.arange(-20, 20, 0.5)
X, Y = np.meshgrid(X, Y)
Z = B*(2*a-np.sqrt(X**2+Y**2))*np.exp(-np.sqrt(X**2+Y**2)/(2*a))
outputimg(X, Y, Z)


# 3

X = np.arange(-20, 20, 0.5)
Y = np.arange(-20, 20, 0.5)
X, Y = np.meshgrid(X, Y)
Z = C*X*np.exp(-np.sqrt(X**2+Y**2)/(2*a))
outputimg(X, Y, Z)
# 4

X = np.arange(-20, 20, 0.5)
Z = np.arange(-20, 20, 0.5)
X, Y = np.meshgrid(X, Y)
Y = D*(2*Z**2-X**2)*np.exp(-np.sqrt(X**2+Z**2)/(3*a))
outputimg(X, Z, Y)

plt.show()