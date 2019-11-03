import pandas as pd
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import make_classification  
from sklearn.neighbors import KNeighborsClassifier  
from sklearn.ensemble import RandomForestClassifier  
from sklearn.model_selection import train_test_split  
from sklearn.metrics import roc_curve  
from sklearn.metrics import roc_auc_score  
import numpy as np
import matplotlib.pyplot as plt
data=pd.read_csv('Social_Network_Ads.csv',delimiter=',')
df= data[["Gender","Age","EstimatedSalary"]]
#X, y = load_iris(return_X_y=True)
print(df)
d=data.dropna()
#print(d)
Z=d['Gender'].values.reshape(-1,1)
X=d['Age'].values.reshape(-1,1)
Y=d['EstimatedSalary'].values.reshape(-1,1)
print(X)
print(Y)
print(Z)
X_train, X_test, y_train, y_test = train_test_split(X,Y,test_size=0.2)

clf = LogisticRegression(random_state=0, solver='lbfgs',multi_class='multinomial').fit(X_train, y_train)
ypred=clf.predict(X_test)
print(ypred)
yPro=clf.predict_proba(X_test) 
print(yPro)
sc=clf.score(X_test, y_test)
print(sc)

cm = confusion_matrix(y_test,ypred)

print(cm)

data_X, class_label = make_classification(n_samples=1000, n_classes=2, weights=[1,1], random_state=1)  
X_train, X_test, y_train, y_test = train_test_split(data_X, class_label, test_size=0.3, random_state=1)  
def plot_roc_curve(fpr, tpr):  
    plt.plot(fpr, tpr, color='orange', label='ROC')
    plt.plot([0, 1], [0, 1], color='darkblue', linestyle='--')
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('Receiver Operating Characteristic (ROC) Curve')
    plt.legend()
    plt.show()

model = RandomForestClassifier()  
model.fit(X_train, y_train) 
probs = model.predict_proba(X_test) 
probs = probs[:, 1]  
auc = roc_auc_score(y_test, probs)  
print('AUC: %.2f' % auc)      
fpr, tpr, thresholds = roc_curve(y_test, probs)  
plot_roc_curve(fpr, tpr)  