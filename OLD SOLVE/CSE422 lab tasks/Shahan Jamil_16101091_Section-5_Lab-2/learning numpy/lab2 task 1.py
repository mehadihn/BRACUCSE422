

import numpy as np
    
def factorial( count ):
   if count <1:   # base case
       return 1
   else:
       returnNumber = count * factorial( count - 1 )  # recursive 
      
       return returnNumber

array=np.zeros(5)

for i in np.arange(0,5):
    array[i]=int(input("please enter number"))
for i in np.arange(0,5):
    print("Factorial of ",array[i]," is ",factorial(array[i]))