import numpy as np
data = np.array([[1, -1, 4],
                 [2, 1, 3],
                 [1, 3, -1]])
C = np.cov(data, bias=True)
print(C)
