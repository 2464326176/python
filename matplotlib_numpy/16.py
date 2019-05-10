import numpy as np
import sympy

M = (2**np.e)*np.math.factorial(2)

u = sympy.Symbol('u')
P = 1/M*(u**2-1)**np.e

print(P)
p2 = sympy.diff(P, u, 2)

# print(p2)