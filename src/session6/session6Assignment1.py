# Problem Statement 1:

# Write a function so that the columns of the output matrix are powers of the input
# vector.
# The order of the powers is determined by the increasing boolean argument. Specifically,
# when increasing is False, the i-th output column is the input vector raised element-wise
# to the power of N - i - 1.

# HINT: Such a matrix with a geometric progression in each row is named for Alexandre-
# Theophile Vandermonde.
import numpy as np


def customVander(x, N=None, increasing=False):
    ndArray = np.array(x)
    N = len(x) if N is None else N
    if(not(increasing)):
        outputArray = np.column_stack([ndArray**(N-1-i) for i in range(N)])
    else:
        outputArray = np.column_stack([ndArray**i for i in range(N)])
    return outputArray


a = [1, 3, 5, 6]
N = 4
outMat = customVander(a, increasing=True)
print(outMat)
