import numpy as np
import sympy as sp
import math
from sympy import Symbol, sqrt
from sympy.vector import CoordSys3D
from sympy.physics.vector import ReferenceFrame, cross, dot
N = CoordSys3D('N')
t = Symbol('t')
r = ((1)*N.i) + ((-2)*N.j) + ((1)*N.k)
v = ((3)*N.i) + ((0)*N.j) + ((4)*N.k)
a = ((5)*N.i) + ((2)*N.j) + ((0)*N.k)
tanVec = (r/(sqrt(r & r)))
normVec = ((v ^ (a ^ v))/(sqrt(v & v) * sqrt((v ^ a) & (v ^ a))))
binormVec = ((v ^ a )/(sqrt((v ^ a) & (v ^ a))))
print("Vetor Tangente: ", tanVec)
print("Vetor Normal: ", normVec)
print("Vetor Binormal: ", binormVec)
