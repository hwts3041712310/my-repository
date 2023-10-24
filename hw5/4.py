import numpy as np
A = np.array([[2, 1], [4, 5]])
n = A.shape[0]
x = np.random.randn(n)
max = 1000
tol = 1e-6
for i in range(max):
    y = np.dot(A, x)
    a = np.dot(x, y) / np.dot(x, x)
    err = np.linalg.norm(y - a * x)
    if err < tol:
        break
    x = y / np.linalg.norm(y)
print('最大特征值为：', a)
