# #*Printing rational number value *#
import sympy as sym
#!Rational number value

ar = sym.Rational(1, 2)
print(ar.evalf())

br = sym.pi**2
print(br.evalf())

cr = sym.pi.evalf()
print(cr+(sym.exp(1)).evalf())

x = sym.Symbol('x')
y = sym.Symbol('y')
print(x+y-x+y);

#!Algebraic number value

aFormula = sym.expand((x+y)**3)
print(aFormula)

bTrigo = sym.expand(sym.sin(x+y), trig=True)
print(bTrigo)

cSimplify = ((x+x*y)/x).simplify()
print(cSimplify)

#! Calculus the value of a formula
aCalc = sym.limit(sym.sin(x)/x , x, 00) 
print(aCalc)

bCalc = sym.diff(sym.sin(x),x)
print(bCalc)

cCalc = sym.integrate(sym.sin(x),x)
print(cCalc)

dCalc = sym.series(sym.exp(x),x)
print(dCalc)

#! Equation solving

aEqu = sym.solve(x**2-1, x)
print(aEqu)

bEqu = sym.Matrix([[1,2],[4,5]])
print(bEqu**(2))