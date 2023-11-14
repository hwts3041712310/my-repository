from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
from sklearn.datasets import fetch_20newsgroups
from sklearn.model_selection import train_test_split

data = fetch_20newsgroups()

x_train, x_test, y_train, y_test = train_test_split(data.data, data.target, test_size=0.2, random_state=22)

model = make_pipeline(TfidfVectorizer(), MultinomialNB())
model.fit(x_train, y_train)

y_pred = model.predict(x_test)

print("score:", model.score(x_test, y_test))
