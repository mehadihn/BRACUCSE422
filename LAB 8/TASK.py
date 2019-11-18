# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
from sklearn import tree
import random

data = pd.read_csv("data.csv")
#print(data.head())

"""
We just changed Color attribute to reflect 0 for Red and 1
for Blue. Similarly, we substituted 0 for Snickers and 1
for Kit Kat in the column Brand.
"""

data['Color'] = data['Color'].map({'Red': 0, 'Blue': 1})
data['Brand'] = data['Brand'].map({'Snickers': 0, 'Kit Kat': 1})

#$print(data.head())

"""
One last thing: it’s a convention to denote our
training attributes by X and output class by Y,
so we will do that now
"""

predictors = ['Color', 'Brand']
X = data[predictors]
Y = data.Class

"""
Almost done. We’re ready to train our decision
tree now. Add the following two lines to train
the tree on our data
"""

decisionTreeClassifier = tree.DecisionTreeClassifier(criterion="entropy")
dTree = decisionTreeClassifier.fit(X, Y)

"""
8)	Done? Let’s quickly visualize the tree.
Add these lines and run the program:
"""

dotData = tree.export_graphviz(dTree, out_file=None)
print(dotData)

#print(dTree.predict([[1, 1]]))
#print(dTree.predict([[0, 0]]))


data.insert(2, "Taste", "Bitter")   


taste = ['Bitter' , 'Sweet']

for i in range (len(data)):
    data.Taste[i] = random.choice(taste)

#print(data.head())

data['Taste'] = data['Taste'].map({'Bitter': 0, 'Sweet': 1})
#print(data.head())

predictors = ['Color', 'Brand', 'Taste']
X = data[predictors]
Y = data.Class


decisionTreeClassifier = tree.DecisionTreeClassifier(criterion="entropy")
dTree = decisionTreeClassifier.fit(X, Y)

"""
8)	Done? Let’s quickly visualize the tree.
Add these lines and run the program:
"""

dotData = tree.export_graphviz(dTree, out_file=None)
#print(dotData)

#print(dTree.predict([[1, 1, 1]]))
#print(dTree.predict([[0, 0]]))



