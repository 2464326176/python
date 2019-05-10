from numpy import *
import numpy.random as random
import matplotlib as mpl
import matplotlib.pyplot as plt




# a = [1, 2, 3 ,4]
# a = array(a)
# b = ([1, 2, 3, 4])
# # print(a + b)
# # print(a[:2] + a[-2:])
# a.shape = 2, 2
# print(a.shape)
a =linspace(0, 2**pi, 21)

b = sin(a)

# plt.plot(a, sin(a), 'r-^')
# plt.plot(a, b)
# plt.plot(a, sin(a), '*',
#     a, sin(a * a), '-')
# x = linspace(0, 2 * pi, 50)
# plt.plot(sin(x))
# plt.plot(a, sin(a), 'b-o',
#     a, sin(2 * a), 'r-^')
# plt.plot(a, sin(a), 'bo')
x = random.rand(200)
y = random.rand(200)
size = random.rand(200) * 30
color = random.rand(200)
plt.scatter(x, y, size, color)
# 显示颜色条
plt.colorbar()
plt.show()