import numpy as np
data = np.array([[1, -1, 4],
                 [2, 1, 3],
                 [1, 3, -1]])
A = np.cov(data, bias=True)
val,vec = np.linalg.eig(A)
for i in range(len(val)):
    print(f'特征值：{val[i]}')
    print(f'特征向量:{vec[i]}')

