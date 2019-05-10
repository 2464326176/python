import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

# 一维无线深势的粒子波函数图像
'''
ψn(x)=√(2/a)sin(nπ/a x)
波函数的归一化常数与能级的级次无关 与势阱宽度的平方根成反比

'''
plt.figure()

a = 4
n = 2  # 量子数

t = np.arange(0, 1, 0.01)

s = np.sqrt(2/a)*np.sin(n*np.pi*t)
plt.plot(t, s)

plt.ylabel('y')
plt.xlabel('x')

plt.title('一维无线深势')
plt.show()
