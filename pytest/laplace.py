from vetores import *
from sympy.integrals import laplace_transform
from sympy.integrals.transforms import inverse_laplace_transform
from sympy.abc import t, s, a
# f = (sin(t) + E**(-t))**2
f = (sin(t))**2
# F = s**2/(s**2 + 64)**2
# F = s/(s**4 + 64)
# F = (s**2 - 6*s + 4)/(s**3 - 3*s**2 + 2*s)
print(laplace_transform(f, t, s))
# print(inverse_laplace_transform(F, s, t))
 