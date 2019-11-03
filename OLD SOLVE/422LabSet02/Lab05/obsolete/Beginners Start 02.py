import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn import model_selection, preprocessing
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
# using data as numpy array
dt = datasets.load_iris()
print(dt.data)
print("\ndata shape ",dt.data.shape)
#import data as dataframe
df = pd.DataFrame(dt.data, columns=dt.feature_names)
print(df.head())

# since it does not have any class feature column creating random feature
v = np.random.randint(0,100,dt.data.shape[0])
v = v.reshape(v.shape[0],1)
binary = preprocessing.Binarizer(threshold=50)
binary_class_values = binary.transform(v) 
print("shape is differnt than input",binary_class_values.shape)

# reshaped to 150,1
class_data = binary_class_values.reshape(dt.data.shape[0],1)

# first convert pandas dataframe into dataseries or numpy array
input_data = df.values

# add the column with the input_data
whole_dataset = np.c_[dt.data,class_data]

# split into input and output
input_x = whole_dataset[:, 0:4]
output_y = whole_dataset[:, -1:]

train_x, test_x, train_y, test_y = model_selection.train_test_split(input_x, output_y, test_size=0.2)

train_y=train_y.reshape(train_y.shape[0])
test_y=test_y.reshape(test_y.shape[0])

models = []
models.append(('LR', LogisticRegression()))
models.append(('LDR', LinearDiscriminantAnalysis()))
models.append(('SVM', SVC()))
models.append(('NB', GaussianNB()))
models.append(('CART', DecisionTreeClassifier()))
models.append(('KNN', KNeighborsClassifier()))

name = []
results = []

for n, model in models:
    kfold = model_selection.KFold(n_splits=10, random_state=7)
    cv_results = model_selection.cross_val_score(model, train_x, train_y, cv=kfold, scoring='accuracy')
    results.append(cv_results)
    name.append(n)
    msg = "%s: %f (%f)" %(n, cv_results.mean(), cv_results.std())
    print(msg)
    
    
# Compare Algorithms
fig = plt.figure()
fig.suptitle('Algorithm Comparison')
ax = fig.add_subplot(111)
plt.boxplot(results)
ax.set_xticklabels(name)
plt.show()
    
    
# Make predictions on validation dataset
knn = KNeighborsClassifier()
knn.fit(train_x, train_y)
predictions = knn.predict(test_x)
print("\nPredictions: ",predictions)
print("\naccuracy score ",accuracy_score(test_y, predictions))
print("\nconfusion_matrix",confusion_matrix(test_y, predictions))
print("\nclassification_report",classification_report(test_y, predictions))
    
    
