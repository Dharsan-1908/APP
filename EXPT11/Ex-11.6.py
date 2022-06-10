from sre_constants import SRE_INFO_PREFIX
from sympy import *

#derivatives
x = Symbol('x')

#log
ans1 = diff(log(x),x)
print(ans1)

# 1/x
ans2 = diff(1/x,x)
print(ans2)

# sinx
ans3 = diff(sin(x),x)
print(ans3)

# cosx
ans4 = diff(cos(x),x)
print(ans4)

# x
ans5 = diff(x,x)
print(ans5)
