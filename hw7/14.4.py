from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn import metrics

newsgroups = fetch_20newsgroups(subset='all', remove=('headers', 'footers', 'quotes'))
text_data = newsgroups.data
labels = newsgroups.target

tfidf_vectorizer = TfidfVectorizer()
tfidf_vectors = tfidf_vectorizer.fit_transform(text_data)

x_train, x_test, y_train, y_test = train_test_split(tfidf_vectors, labels, test_size=0.2, random_state=22)

naive_bayes_classifier = MultinomialNB()
naive_bayes_classifier.fit(x_train, y_train)
y_pred = naive_bayes_classifier.predict(x_test)

accuracy = metrics.accuracy_score(y_test, y_pred)
print("准确度:",accuracy)

