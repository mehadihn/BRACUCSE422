sum=0
c=0
for x in range(100):
    if x%3==0 and x!=0:
        sum+=x
        c=c+1
print("Average:",sum/c)    