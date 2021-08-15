from sympy.vector.operators import divergence
from vetores import *

f = N.x*N.y*N.z
# F = ((-3*1+E**(N.y*N.z))*N.i) - ((E**(N.x*N.z))*N.j) + ((3*N.z*((N.x**2)+(N.y**2)))*N.k)
F = ((-3*N.y**3*N.z)*N.i) - ((sin(N.x*N.z))*N.j) - ((2*N.z**2*((N.x**2)+(N.y**2)))*N.k)
G = ((3*N.x*N.y*N.z**2)*N.i) + ((2*N.x*N.y**3)*N.j) + ((-1*N.x**2*N.y*N.z)*N.k)
# F = (N.x + N.y)
# print("gradF: ",gradient(F))
# print("divF: ", divergence(F))
print("rotF: ",curl(F))

# print(F.dot(gradient(f)))
# print((F & delop)(f))
# print(avecOp(F, f))