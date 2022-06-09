from os import system
from sympy import *

#solving matrix linear equation

x  = Symbol('x')
y  = Symbol('y')
z  = Symbol('z')

equ1 = Eq(3*x+7*y-12*z,0)
equ2 = Eq(4*x-2*y-5*z,0)

ans = solve([equ1,equ2], (x,y,z))

print(ans)

