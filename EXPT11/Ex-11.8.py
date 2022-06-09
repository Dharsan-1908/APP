from sympy import *

x = Symbol('x')
y = Symbol('y')

#x^2
ans1 = integrate(x**2,x,y)
print(ans1)

#sinx
ans2 = integrate(sin(x),x,y)
print(ans2)

#cosx
ans3 = integrate(cos(x),x,y)
print(ans3)

