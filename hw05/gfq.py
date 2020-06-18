import sympy as sp
x=sp.Symbol('x')
f=((300+x)**4-8100000000)*4.8195/7536/10000 + x*500/6/3.14-x+61.875
x=sp.solve(f)
print(x)