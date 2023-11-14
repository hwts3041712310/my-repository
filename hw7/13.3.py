from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
iris = load_iris()

x = iris.data
y = iris.target

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=23)
knn = KNeighborsClassifier(n_neighbors=3) 
knn.fit(x_train, y_train)

train_prediction= knn.predict(x_train)
train_accuracy = accuracy_score(y_train, train_prediction)

print("训练集准确度：", train_accuracy)

test_prediction= knn.predict(x_test)
test_accuracy = accuracy_score(y_test, test_prediction)

print("测试集准确度：", test_accuracy)
