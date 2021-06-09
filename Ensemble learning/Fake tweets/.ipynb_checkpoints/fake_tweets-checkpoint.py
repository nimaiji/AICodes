import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree

real_tweets = pd.read_csv('pol-real.csv')
fake_tweets = pd.read_csv('pol-fake.csv')

real_tweets_len = len(real_tweets)
fake_tweets_len = len(fake_tweets)

new_real = real_tweets.assign(real=real_tweets_len * [1])
new_fake = fake_tweets.assign(real=fake_tweets_len * [0])

dataset = pd.concat([new_real, new_fake]).sample(n=real_tweets_len + fake_tweets_len)
# dataset.to_csv('dataset.csv', index=False)

data_train, data_test = train_test_split(dataset,test_size=0.2,train_size=0.8)
# data_train.to_csv('data-train.csv', index=False)
# data_test.to_csv('data-test.csv', index=False)

# Default criterion is Gini
dtc = DecisionTreeClassifier()
dtc = dtc.fit(data_train,data_train['real'])
tree.plot_tree(dtc)
plt.show()



