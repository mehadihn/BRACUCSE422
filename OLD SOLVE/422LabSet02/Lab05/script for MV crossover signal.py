import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#read input
dataset = pd.read_csv('GBPUSD2000_2018.csv', header=0, index_col=0)
#print(dataset.head(),"\n",dataset.describe())

#taking moving averages of 28 days and 260 days sliding window method
real = dataset.Close
mv1 = dataset.Close.rolling(28).mean()
mv2 = dataset.Close.rolling(260).mean()

# convert series to frame
mv1 = mv1.to_frame()
mv2 = mv2.to_frame()
diff = mv1 - mv2

# adding new header in the column
mv1.columns = ['MA1']
mv2.columns = ['MA2']
diff.columns= ['diff']

# Adding all the columns together
frames = [real, mv1, mv2, diff]
total = pd.concat(frames, axis=1)

# check whether it contains any Nan value
print(total.head())

#drop row if there is any value zero within a row
final = total.dropna(axis=0, how="any")

# check whether it contains any Nan value after applying dropna
print(final.head())

# see the results in charts
#final[['Close','MA1','MA2']].plot(figsize=(20,10))
#plt.show()

# below is the logic when to start selling and when to buy
X = 0.05
final['dec'] = np.where(final['diff'] > X, 1, 0)
final['dec'] = np.where(final['diff'] < X, -1, final['dec'])
print("Total number of buy and Sell Signal \n",final['dec'].value_counts())

# charting the decision 
#final['dec'].plot(figsize=(20, 10))
#plt.show()

# put all together in one chart to compare the accuracy of our strategy
plt.figure(figsize=(6, 4))
plt.subplot(2, 1, 1)
final[['Close','MA1','MA2']].plot(ax=plt.gca())
plt.subplot(2, 1, 2)
final['dec'].plot()
plt.xticks(())
plt.yticks(())
plt.text(0.1, 0.5, 'Buy Sell Decision', ha='center', va='center',size=10, alpha=.5)
plt.tight_layout()
plt.show()

# ignore the following code just for referencing purpose for future use

#Create an "empty" column as placeholder for our /position signals
##final['decision'] = None
##
##for row in range(len(final)):
##   if (final['diff'].iloc[row] > X) and (final['Close'].iloc[row] > final['MA2'].iloc[row]):
##        final['decision'].iloc[row] = 1
##   if (final['diff'].iloc[row] < X) and (final['Close'].iloc[row] < final['MA2'].iloc[row]):
##        final['decision'].iloc[row] = -1  
##
##print(final['decision'].value_counts())
