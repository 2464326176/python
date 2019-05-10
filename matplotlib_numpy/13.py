from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt
import numpy as np

# 定义基始初量
A = 1
B = 2

# 定义输出图像函数
def outputimg(X,Y,Z):

    fig = plt.figure()
    ax = fig.gca(projection='3d')
    surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.coolwarm,linewidth=0, antialiased=False)
    ax.set_zlim(-1.01, 1.01)
    ax.zaxis.set_major_locator(LinearLocator(10))
    ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
    fig.colorbar(surf, shrink=0.5, aspect=5)

# 1

# X = np.arange(-10, 10, 0.1)  #定义为半径范围
# Y = 1
# # X, Y = np.meshgrid(X, Y)
# Z = A*np.exp(-B*X)*np.sqrt(1/(4*np.pi))*Y
# # outputimg(X, Y, Z)
# plt.plot(X, Z)

# X = np.arange(-10, 10, 0.5)  #定义为半径范围
# Y = np.arange(-np.pi, np.pi, 0.5)
# X, Y = np.meshgrid(X, Y)
# Z = A*X*np.exp(-B*X/2)*np.sqrt(3/(4*np.pi))*np.cos(Y)
# outputimg(X, Y, Z)

# X = np.arange(-100, 100)
# Y = np.arange(-np.pi, np.pi)
# X, Y = np.meshgrid(X, Y)
# Z = A*X*np.exp(-B*X/2)*np.sqrt(3/(4*np.pi))*np.cos(Y)
# outputimg(X, Y, Z)


X = np.arange(-np.pi, np.pi)
Y = np.arange(-np.pi, np.pi)
X, Y = np.meshgrid(X, Y)
Z = np.sin(X)*np.cos(Y)
outputimg(X, Y, Z)





plt.show()













