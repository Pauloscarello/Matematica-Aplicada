import numpy as np
u1 = int(input("u1: "))
u2 = int(input("u2: "))
u3 = int(input("u3: "))
u=np.array([u1, u2, u3])
print("Norma: raiz(%d)"% np.dot(u, u))