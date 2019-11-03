import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv('Annual-risk.csv', delimiter = ',')
#print(df)
#print(df[['Age Range']])

x = df['Age Range']
y = df['Female']
z = df['Male']

plt.plot(x,y, label ="Female")
plt.plot(x,z, label = "Male")
plt.legend()
plt.show()