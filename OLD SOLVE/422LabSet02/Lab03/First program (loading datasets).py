import pandas as pd
from sklearn import datasets
import matplotlib.pyplot as plt

# loading builtin default from skicit learn
dt = datasets.load_boston()
#similarly we can load irish flower dataset, or cancer datasets
# press tab after datasets. then it will show list of available datasets
print(dt.data)
# why dt.data? just print dt it will show you whole information about datasets 
# print feaures name, check target name, target values 


# loading another default dataset from skicit learn
digit = datasets.load_digits()
print(digit.images[4])
# now to see what does the matrix represent we can write 
# plt.imshow(dt.images[4], cmap=plt.cm.gray_r, interpolation='nearest')
# plt.show()
# try other mapping plt.imshow(dt.images[4], cmap=plt.cm.CMRmap)


#import data as dataframe (converting numpy array to dataframe)
df = pd.DataFrame(dt.data, columns=dt.feature_names)
print(df.head())

# can you convert dataframe to numpy array?
