from sympy import *

# expanding using sympy

x = Symbol('x')
y = Symbol('y')

ans = expand((x+y)**6)
print(ans)