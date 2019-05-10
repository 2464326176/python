import sympy

x = sympy.Symbol('x')

print(sympy.diff(sympy.sin(x), x))
print(sympy.diff(sympy.sin(x), x, 2))#2阶导数
print(sympy.diff(sympy.sin(x), x, 3))#2阶导数
print(sympy.diff(sympy.sin(x), x, 4))#2阶导数