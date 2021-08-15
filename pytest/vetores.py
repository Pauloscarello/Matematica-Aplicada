import math
from fractions import *
from sympy import *
from sympy.abc import x, y, z
from sympy.vector import CoordSys3D, curl, divergence, gradient, Del
from sympy.physics.vector import ReferenceFrame, cross, dot, dynamicsymbols
N = CoordSys3D('N')
t = Symbol('t')
a = Symbol('a')
delop = Del()
# r = ((t**2*sin(1*t))*N.i) + ((t**2*cos(1*t))*N.j) + ((t**2*cos(2*t))*N.k)
# r = ((1*sin(1*t))*N.i) + ((1*cos(1*t))*N.j) + ((2*t**2)*N.k)
# rPrime = r.diff(t)
# print(rPrime)
# print(rPrime.subs(t, math.pi))
VecT = ((-1/math.sqrt(3))*N.i) + ((1/math.sqrt(3))*N.j) + ((1/math.sqrt(3))*N.k)
VecN = ((-1/math.sqrt(3))*N.i) + ((1/math.sqrt(3))*N.j) + ((1/math.sqrt(3))*N.k)
VecB = ((0)*N.i) + ((-1/math.sqrt(2))*N.j) + ((1/math.sqrt(2))*N.k)
# print("\nVetor N: ", (VecB ^ VecT))
# print("\nVetor T: ", (VecN ^ VecB))
# print(math.sqrt(2)/math.sqrt(3))
# print(1/math.sqrt(6))

def norm(x1, x2, x3):
    vetorX = x1*N.i + x2*N.j + x3*N.k
    normaX = sqrt(vetorX & vetorX)
    return normaX

def BxT(b1, b2, b3, t1, t2, t3):
    vetorB = b1*N.i + b2*N.j + b3*N.k
    vetorT = t1*N.i + t2*N.j + t3*N.k
    return vetorB ^ vetorT

def NxB(n1, n2, n3, b1, b2, b3):
    vetorN = n1*N.i + n2*N.j + n3*N.k
    vetorB = b1*N.i + b2*N.j + b3*N.k
    return vetorN ^ vetorB

def TxN(t1, t2, t3, n1, n2, n3):
    vetorT = t1*N.i + t2*N.j + t3*N.k
    vetorN = n1*N.i + n2*N.j + n3*N.k
    return vetorT ^ vetorN

def anguloUV(u1, u2, u3, v1, v2, v3):
    vetorU = u1*N.i + u2*N.j + u3*N.k
    vetorV = v1*N.i + v2*N.j + v3*N.k
    anguloRad = acos((vetorU & vetorV)/(norm(u1, u2, u3) * norm(v1, v2, v3)))
    return anguloRad

def areaUV(u1, u2, u3, v1, v2, v3):
    vetorU = u1*N.i + u2*N.j + u3*N.k
    vetorV = v1*N.i + v2*N.j + v3*N.k
    areaParalelogramo = sqrt((vetorU ^ vetorV) & (vetorU ^ vetorV))
    return areaParalelogramo

def Prime(r):
    return simplify(r.diff(t))

def Prime2(r):
    return simplify(r.diff(t).diff(t))

def Prime3(r):
    return simplify(r.diff(t).diff(t).diff(t))

def torsion(r, valor):
    # t = a/b
    # a = r' x r'' . r'''
    a = Prime(r).cross(Prime2(r)).dot(Prime3(r))
    # b = || r' x r'' ||²
    b = (Prime(r).cross(Prime2(r))).magnitude()
    return simplify(a.subs(t, valor))/simplify(b.subs(t, valor)*b.subs(t, valor))

def avecOp(F, f):
    return (F & delop)(f)

def derivaX(F):
    return F.diff(x).simplify()

def derivaY(F):
    return F.diff(y).simplify()

def derivaZ(F):
    return F.diff(z).simplify()

def norma(u):
    uU = u.dot(u)
    norma = sqrt(uU)
    return norma

def acelT(r):
    return (Prime(r) & Prime2(r))/norma(Prime(r))

def acelN(r):
    return (Prime(r) ^ Prime2(r))/norma(Prime(r))


# ((rPrime.subs(t, valor) ^ rPrimePrime.subs(t, valor)) & rPrimePrimePrime.subs(t, valor))/(sqrt((rPrime.subs(t, valor) ^ rPrimePrime.subs(t, valor)) & (rPrime.subs(t, valor) ^ rPrimePrime.subs(t, valor))) * sqrt((rPrime.subs(t, valor) ^ rPrimePrime.subs(t, valor)) & (rPrime.subs(t, valor) ^ rPrimePrime.subs(t, valor))))
# areaP = (areaUV(1, 1, 7, 1, 2, 2)) 

# print("Área Paralelogramo: ", areaP)
# print("Ângulo em graus: ", anguloRadianos/np.pi * 180)

# Tdel = derivaX((x*y)/(1+x**2+y**2))*N.i + derivaY((x*y)/(1+x**2+y**2))*N.j
# a = 2*N.i - N.j
# u = a/norma(a)
# print(u.dot(Tdel.subs({x:1, y:1})))
# print((Tdel.subs({x:1, y:1}))/norma((Tdel.subs({x:1, y:1}))))