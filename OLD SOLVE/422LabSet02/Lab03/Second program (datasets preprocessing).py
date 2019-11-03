import numpy as np
from sklearn import preprocessing

input_data = np.array([[5.1, -2.9, 3.3],
                       [-1.2, 7.8, -6.1],
                       [3.9, 0.4, 2.1],
                       [7.3, -9.9, -4.5]]) 
# only binarized data depend on positive and negetive
binarized = preprocessing.binarize(input_data)
print("binarized data\n",binarized)

# binarized data threshold value 2.1 hence values lower than 2.1 will be 0 and above 1
binarized = preprocessing.Binarizer(threshold=2).transform(input_data)
print("\nNew binarized\n",binarized)

# calculation column wise
print("Mean of the given data", input_data.mean(axis=0))  
print("Standard Deviation of the given data", input_data.std(axis=0))

# After scaling
scaled = preprocessing.scale(input_data)
print("Mean of the given data", scaled.mean(axis=0))  
print("Standard Deviation of the given data", scaled.std(axis=0))

# Minmax scaling
scale_range = preprocessing.MinMaxScaler(feature_range=(0,1))
scaled = scale_range.fit_transform(input_data)
print(scaled)

# normalize data
norm_l1_data = preprocessing.normalize(input_data, norm = 'l1') 
print("\n normalized L1 data\n",norm_l1_data)

norm_l2_data = preprocessing.normalize(input_data, norm = 'l2') 
print("\n normalized L2 data\n",norm_l2_data)

# can you merge two array rowwise and columnwise (norm_l1_data and norm_l2_data) and normalize them again using numpy concatenate method

# following example given for learning
a = np.arange(10).reshape(5,2)
b = np.arange(20).reshape(10,2)
#print(a,"\n",b)
c = np.concatenate((a,b))
d = np.concatenate((a,b), axis=1)
print(c,d,c.shape, d.shape)
