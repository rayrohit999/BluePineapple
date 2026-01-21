'''
Matrix Ops (Dot, Transpose, Identity)
 - Generate two matrices A (3x4) and B (4x2).
 -Compute A @ B.
 -Verify properties: (A.T).T equals A; create identity matrix I and show A @ I (shape permitting).
'''

import numpy as np
A = np.arange(5, 17)
A.shape = (3, 4)
print("A =", A)

B = np.arange(50,58)
B.shape = (4, 2)
print("\nB=", B)

dotProduct = A @ B
print("\nDot produtct: \n", dotProduct)


#Verifying (A.T).T = A
print("\nVerifying (A.T).T = A:")
print(np.array_equal((A.T).T, A))

I = np.eye(4)
print("\n Identity Matrix: \n", I)
print("\n Shpae permitting (equality check should be True):\n", np.array_equal(A @ I, A))