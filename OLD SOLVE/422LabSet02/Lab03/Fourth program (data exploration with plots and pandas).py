import pandas as pd
from sklearn import datasets
import matplotlib.pyplot as plt

# We know this is a numpy array
#numpy.ndarray 
# your data could be data frame/simple array/numpy array
# So you need to convert your dataset into dataframe like below
input_data = datasets.load_breast_cancer()
#data=input_data.values
print(input_data)

dt = pd.DataFrame(input_data.data, columns=input_data.feature_names)
print(dt.head())
print(dt.describe())

dt.plot(kind='box', subplots=True)
plt.show()

dt.hist()
plt.show()

pd.tools.plotting.scatter_matrix(dt)
plt.show()

# can you explain to your friends beside you what these charts means?

# can you now do this for one to one feature analysis using the above three types of charts, so that you can see how one feature is correlated with another particular feature  
 
