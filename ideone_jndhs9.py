import pandas as pd
fromsklearn.model_selection import train_test_split fromsklearn.feature_extraction.text import CountVectorizer from sklearn.naive_bayes import MultinomialNB
fromsklearn.metrics import accuracy_score, confusion_matrix, precision_score, recall_score
msg = pd.read_csv('document.csv', names=['message', 'label']) print("Total Instances of Dataset: ", msg.shape[0]) msg['labelnum'] = msg.label.map({'pos': 1, 'neg': 0})
X = msg.message y = msg.labelnum
Xtrain, Xtest, ytrain, ytest = train_test_split(X, y) count_v = CountVectorizer()
Xtrain_dm = count_v.fit_transform(Xtrain) Xtest_dm = count_v.transform(Xtest)
df = pd.DataFrame(Xtrain_dm.toarray(),columns=count_v.get_feature_names())
clf = MultinomialNB() clf.fit(Xtrain_dm, ytrain) pred = clf.predict(Xtest_dm)
print('Accuracy Metrics:')
print('Accuracy: ', accuracy_score(ytest, pred)) print('Recall: ', recall_score(ytest, pred)) print('Precision: ', precision_score(ytest, pred))
print('Confusion Matrix: \n', confusion_matrix(ytest, pred))
