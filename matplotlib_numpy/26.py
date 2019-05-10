import numpy as np
a = np.array([[0, 1, 0],
              [1, 0, 1],
              [0, 1, 0]])
b = np.linalg.eig(a)


print(b)