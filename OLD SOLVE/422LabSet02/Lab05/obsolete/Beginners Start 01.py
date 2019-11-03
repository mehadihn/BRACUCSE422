import numpy as np
import pandas as pd
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn import datasets
from sklearn.naive_bayes import GaussianNB
from sklearn.cross_validation import cross_val_score

# loading datasets
data = datasets.load_breast_cancer()
#print(data.data,data.target)

# declaring classifier
#classifier = linear_model.LogisticRegression()
# declaring classifier
#classifier = multiclass.OneVsOneClassifier(svm.LinearSVC(random_state=0))

# declaring classifier
classifier = GaussianNB()

train_x, test_x, train_y, test_y = train_test_split(data.data, data.target, test_size=0.2, random_state=7)

# train my classifier
classifier.fit(train_x, train_y)

# testing the data
prediction = classifier.predict(test_x)
print(prediction)

# accuracy of prediction
score_a = cross_val_score(classifier, train_x, train_y, scoring='accuracy', cv=3)
score_pw = cross_val_score(classifier, train_x, train_y, scoring='precision_weighted', cv=3)
score_rw = cross_val_score(classifier, train_x, train_y, scoring='recall_weighted', cv=3)
score_fw = cross_val_score(classifier, train_x, train_y, scoring='f1_weighted', cv=3)
print("\nscore\n",score_a,"\n",score_pw,"\n",score_rw,"\n",score_fw)

