from sympy.physics.vector.fieldfunctions import divergence
from vetores import divergence, ln, E
from sympy.abc import x, y
v1 = ln(1 + x**2) + E**y
divergence(v1)
