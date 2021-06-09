import matplotlib.pyplot as plt
import pandas as pd
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, balanced_accuracy_score
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.tree import DecisionTreeClassifier

__author__ = "Nima Iji"
__email__ = "ijinima@gmail.com"

real_tweets = pd.read_csv('pol-real.csv')
fake_tweets = pd.read_csv('pol-fake.csv')

real_tweets_len = len(real_tweets)
fake_tweets_len = len(fake_tweets)

new_real = real_tweets.assign(real=real_tweets_len * [1])
new_fake = fake_tweets.assign(real=fake_tweets_len * [0])

dataset = pd.concat([new_real, new_fake]).sample(n=real_tweets_len + fake_tweets_len)
# dataset.to_csv('dataset.csv', index=False)
columns = list(dataset.keys())[0:35]

y = dataset.real
data_train, data_test, y_train, y_test = train_test_split(dataset[columns], y, test_size=0.2, train_size=0.8,
                                                          shuffle=True)
# data_train.to_csv('data-train.csv', index=False)
# data_test.to_csv('data-test.csv', index=False)

# Default criterion is Gini
print("## First figure:\twith Gini criterion")
dtc = DecisionTreeClassifier()
dtc = dtc.fit(data_train, y_train)
real_pred = pd.DataFrame(dtc.predict(data_test))
real_pred.to_csv('pred.csv', index=False)

plt.figure('Gini', figsize=(7, 5), dpi=120)
tree.plot_tree(dtc)
plt.plot()

print("Confusion matrix: \n{}".format(confusion_matrix(y_test, real_pred)))
print("\nClassification report: \n{}".format(classification_report(y_test, real_pred)))
print("\nBalanced accuracy: {}\n".format(balanced_accuracy_score(y_test, real_pred)))

# Using Information gain method
print("## Second figure:\twith Information gain criterion")
dtc2 = DecisionTreeClassifier(criterion="entropy")
dtc2 = dtc2.fit(data_train, y_train)
real_pred2 = pd.DataFrame(dtc2.predict(data_test))
real_pred2.to_csv('pred2.csv', index=False)

plt.figure('Information gain', figsize=(7, 5), dpi=120)
tree.plot_tree(dtc2)
plt.plot()
print("Confusion matrix: \n{}".format(confusion_matrix(y_test, real_pred2)))
print("\nClassification report: \n{}".format(classification_report(y_test, real_pred2)))
print("\nBalanced accuracy: {}\n".format(balanced_accuracy_score(y_test, real_pred2)))

# 10-Fold Cross validation method
print("## Third figure:\t10-Fold Cross-Validation method")
best_score = 0.0
for i in range(5, 20):
    clf = tree.DecisionTreeClassifier(max_depth=i)
    scores = cross_val_score(estimator=clf, X=dataset[columns], y=y, cv=10)
    if best_score < scores.mean():
        best_score = scores.mean()
print("\nAccuracy: {}\n".format(best_score))

# Random forest classifier
print("## Fourth figure:\tRandom forest")
y = dataset.real
data_train, data_test, y_train, y_test = train_test_split(dataset[columns], y, test_size=0.2, train_size=0.8,
                                                          shuffle=True)
rfc = RandomForestClassifier(n_estimators=20)
rfc = rfc.fit(data_train, y_train)
rfc_pred = rfc.predict(data_test)
print("\nBalanced accuracy: {}".format(balanced_accuracy_score(y_test, rfc_pred)))

plt.show()
