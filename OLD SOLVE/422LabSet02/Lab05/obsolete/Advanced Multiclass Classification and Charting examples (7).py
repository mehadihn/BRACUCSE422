import numpy as np
from matplotlib import pyplot as plt
from sklearn import model_selection, cross_validation
from sklearn import linear_model, datasets
from sklearn import metrics
from sklearn import preprocessing

n_samples = 1000
n_outliers = 50


X, y, coef = datasets.make_regression(n_samples=n_samples, n_features=1,
                                      n_informative=1, noise=10,
                                      coef=True, random_state=0)

# Add outlier data
np.random.seed(0)
X[:n_outliers] = 3 + 0.5 * np.random.normal(size=(n_outliers, 1))
y[:n_outliers] = -3 + 10 * np.random.normal(size=n_outliers)

# declaring classifier
classifier = linear_model.LinearRegression()
train_x, test_x, train_y, test_y = model_selection.train_test_split(X, y, test_size=0.2, random_state=7)

# train my classifier
classifier.fit(train_x, train_y)

# testing the data
prediction = classifier.predict(test_x)
print(prediction)

# accuracy of prediction Compute performance metrics 
print("Linear regressor performance:") 
print("Mean absolute error =", round(metrics.mean_absolute_error(test_y, prediction), 2)) 
print("Mean squared error =", round(metrics.mean_squared_error(test_y, prediction), 2))
print("Median absolute error =", round(metrics.median_absolute_error(test_y, prediction), 2)) 
print("Explain variance score =", round(metrics.explained_variance_score(test_y, prediction), 2)) 

#
# Robustly fit linear model with RANSAC algorithm
ransac = preprocessing.PolynomialFeatures(degree=10) 
ransac.fit(X, y)
inlier_mask = ransac.inlier_mask_
outlier_mask = np.logical_not(inlier_mask)
#
# Predict data of estimated models
line_X = np.arange(X.min(), X.max())[:, np.newaxis]
line_y = classifier.predict(line_X)
line_y_ransac = ransac.predict(line_X)

## Compare estimated coefficients
print("Estimated coefficients (true, linear regression, RANSAC):")
print(coef, classifier.coef_, ransac.estimator_.coef_)

lw = 2
plt.scatter(X[inlier_mask], y[inlier_mask], color='yellowgreen', marker='.',
            label='Inliers')
plt.scatter(X[outlier_mask], y[outlier_mask], color='gold', marker='.',
            label='Outliers')
plt.plot(line_X, line_y, color='navy', linewidth=lw, label='Linear regressor')
plt.plot(line_X, line_y_ransac, color='cornflowerblue', linewidth=lw,
         label='RANSAC regressor')
plt.legend(loc='lower right')
plt.xlabel("Input")
plt.ylabel("Response")
plt.show()


