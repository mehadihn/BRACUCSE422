#import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import warnings
warnings.filterwarnings('ignore')
#https://www.kaggle.com/loknath2017/logistic-regression-in-python
#import matplotlib.pyplot as plt
#import seaborn as sns matplotlib inline
# Input data files are available in the "../input/" directory.
# For example, running this (by clicking run or pressing Shift+Enter) will list the files in the input directory

#import os
#print(os.listdir("../input"))
dataset = pd.read_csv('Social_Network_Ads.csv')
print(dataset)

x = dataset.iloc[:,2:4].values
y= dataset.iloc[:,4].values

# Split the data into Training and Testing set
from sklearn.cross_validation import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.25,random_state=0)

# Feature scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()

x_train = sc.fit_transform(x_train)
x_test = sc.fit_transform(x_test)
#print(x_test)


#print(x_train)
#print(x_test)
#Fitting logistic regression to the training set
from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression(random_state = 0)
classifier.fit(x_train,y_train)

# Predicting the Test set results
y_pred = classifier.predict(x_test)

print(y_pred)

# Making the confusion matrix 
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test,y_pred)

print(cm)

print(sum(y_test))

import numpy as np
from sklearn.metrics import accuracy_score
print(accuracy_score(y_test, y_pred))






