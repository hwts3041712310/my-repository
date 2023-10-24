import numpy as np
A = np.array([[2, 1], [4, 5]])
eigen_values, eigen_vectors = np.linalg.eig(A)
print('特征值:', eigen_values)
print('特征向量:', eigen_vectors)
