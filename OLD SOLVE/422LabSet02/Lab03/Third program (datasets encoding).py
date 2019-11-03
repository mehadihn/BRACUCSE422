import numpy as np
from sklearn import preprocessing

input_data = np.array(['Red',
                       'Green',
                       'Yellow',
                       'Black',
                       'Purple']) 
# Encoding data
encoder = preprocessing.LabelEncoder()
encoded = encoder.fit_transform(input_data)
print(encoded)

for i, item in enumerate(encoder.classes_):
    print(item,'-->',i) 
    
# decoding data    
decoding = encoder.inverse_transform(encoded)
print("\n",decoding)  

# can you do this thing for multiple features
# Here you need to be careful that encoding method does not work with multi-dimentional array
# For an example   
# input array    np.array([['Red','Rose'],['Yellow','Cosmos'],['Purple','Lily']])
# output array   also two dimentional [[0,1],[2,3],[3,4]]  etc

# The following code given as a hint
a = np.array([['Red','Rose'],['Yellow','Cosmos'],['Purple','Lily']])
b = a[:,0]
print(b)
n = encoder.fit_transform(b)
print("\nEncoded values: ",n)

