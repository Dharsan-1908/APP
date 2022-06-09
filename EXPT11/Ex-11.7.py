from sympy import *

#linear equation

x = Symbol('x')
y = Symbol('y')

ans = linsolve([x+y-1, 2*x+y-0],(x,y))

print(ans)