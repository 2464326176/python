import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt


plt.figure()
A1 = 4
Br = 6


R = np.arange(0, 5)
s = A1*R*np.e**(-Br)*np.sqrt(1/np.pi*4)
plt.plot(R, s)
plt.ylabel('y')
plt.xlabel('x')


plt.title('一维无线深势')
plt.show()
