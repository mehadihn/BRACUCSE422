# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 09:11:35 2019

@author: 16101061
"""

import pandas as pd  
import numpy as np  
import matplotlib.pyplot as plt  
import seaborn as seabornInstance 
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression
from sklearn import metrics



data=pd.read_csv('StockPriceData.csv',delimiter=',')
df= data[["Open","Close"]]
print(df)
d=data.dropna()
print(d)
X=d['Open'].values.reshape(-1,1)
Y=d['Close'].values.reshape(-1,1)


plt.scatter(X,Y)
#plt.show()
regressor=LinearRegression()
regressor.fit(X,Y)

xtrain,xtest,ytrain,ytest = train_test_split(X,Y, test_size = 0.5, random_state=42)
linreg = LinearRegression().fit(xtrain, ytrain)
print('R-squared score (training): {:.3f}'
     .format(linreg.score(xtrain, ytrain)))

regressor.fit(xtrain,ytrain)
ypred=regressor.predict(xtest)
print('R-squared score (pred): {:.3f}'
     .format(linreg.score(xtest, ypred)))

plt.plot(xtest,ypred,color='red',linewidth=2)
plt.show()

print (xtrain.shape, ytrain.shape)
print (xtest.shape, ytest.shape)
pred_train=regressor.predict(xtrain)
plt.scatter(xtrain,ytrain,s=3)
plt.plot(xtrain,pred_train,color='green',linewidth=2)
plt.show()

pred_test=regressor.predict(xtest)
plt.scatter(xtest,ytest,s=5)
plt.plot(xtest,pred_test,color='black',linewidth=2)
plt.show()
print('Mean Absolute Error:', metrics.mean_absolute_error(ytest, ypred))  
print('Mean Squared Error:', metrics.mean_squared_error(ytest, ypred))  
print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(ytest, ypred)))