from sympy import *

#limits

x = Symbol('x')

ans = limit((sin(x)-x)/x**3,x,0)

print(ans)