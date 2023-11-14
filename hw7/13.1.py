import matplotlib.pyplot as plt
import pandas as pd
from sklearn.datasets import load_iris
from pandas.plotting import scatter_matrix
iris = load_iris()
data = iris.data
feature_names = iris.feature_names
iris_df = pd.DataFrame(data, columns=feature_names)
iris_df['target'] = iris.target
scatter_matrix(iris_df, alpha=0.9, figsize=(11,11), diagonal='hist')
plt.suptitle("Iris Dataset Features", y=0.95)
plt.show()
