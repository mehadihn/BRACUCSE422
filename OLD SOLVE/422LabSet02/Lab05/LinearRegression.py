import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.cross_validation import train_test_split
from sklearn.datasets import make_regression

# synthetic dataset for simple regression

plt.figure()
plt.title('Sample regression problem with one input variable')
X_R1, y_R1 = make_regression(n_samples = 100, n_features=1,
                            n_informative=1, bias = 150.0,
                            noise = 30, random_state=1)
plt.scatter(X_R1, y_R1, marker= 'o', s=50)
plt.show()


X_train, X_test, y_train, y_test = train_test_split(X_R1, y_R1,
                                                   random_state = 0)
linreg = LinearRegression().fit(X_train, y_train)

print('Output of Least Squares Logistic Regression')

#Task 1:
    
#print('linear model coeff (w): {}'
#     .format(linreg.coef_))
#print('linear model intercept (b): {:.3f}'
#     .format(linreg.intercept_))

print('R-squared score (training): {:.3f}'
     .format(linreg.score(X_train, y_train)))
print('R-squared score (test): {:.3f}'
     .format(linreg.score(X_test, y_test)))

#Plot

plt.figure(figsize=(5,4))
plt.scatter(X_R1, y_R1, marker= 'o', s=10, alpha=0.8)
plt.plot(X_R1, linreg.coef_ * X_R1 + linreg.intercept_, 'r-')
plt.title('Least-squares linear regression')
plt.xlabel('Feature value (x)')
plt.ylabel('Target value (y)')
plt.show()