import numpy as np
import pandas as pd
from sklearn import datasets
from sklearn import model_selection, preprocessing
# using data as numpy array

dt = pd.read_csv('../Lab04/GBPUSD2000_2018.csv', header=0, index_col=0)
#dt = datasets.load_iris()
#print(dt.data)
#print("\ndata shape ", dt.data.shape)
#import data as dataframe
df = pd.DataFrame(dt)
print(df.head())

# since it does not have any class feature column creating random feature
#v = np.random.randint(0,100,dt.data.shape[0])
#print(v.shape,v)
#
##
#v = v.reshape(v.shape[0],1)
#print(v.shape,v)
#binary = preprocessing.Binarizer(threshold=50)
#binary_class_values = binary.transform(v) 
#print("shape is differnt than input",binary_class_values.shape)
#
## reshaped to 150,1
#class_data = binary_class_values.reshape(dt.data.shape[0],1)
#
## first convert pandas dataframe into dataseries or numpy array
#input_data = df.values
#
## add the column with the input_data
#whole_dataset = np.c_[dt.data,class_data]
#
## split into input and output
#input_x = whole_dataset[:, 0:4]
#output_y = whole_dataset[:, -1:]
#
#train_x, test_x, train_y, test_y = model_selection.train_test_split(input_x, output_y, test_size=0.2)
#print(train_x, test_x, train_y, test_y)
#
#print(train_x.shape, test_x.shape, train_y.shape, test_y.shape)
