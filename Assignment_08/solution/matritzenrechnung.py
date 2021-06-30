import numpy as np
import numpy.linalg as lin

v1 = np.array([[1143, 0], [320, 48], [2314, 22]])
v2 = np.array([[123, 2111], [33, 41], [2999, 2861]])

v1_sp1 = v1[:, 0]
v2_sp1 = v2[:, 0]

print(np.cumsum(v1_sp1))
print(np.cumsum(v1, 0)[:, 0])

print(np.cumsum(v2_sp1))
print(np.cumsum(v2, 0)[:, 0])

print(np.min(v1))
print(np.max(v1))

print(np.min(v2))
print(np.max(v2))

print(np.cross(v1, v2))
print(np.dot(v1, v2.T)) # Nicht in Aufgabe gefordert