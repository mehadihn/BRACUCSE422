sum=0
count=0

for v in range(100):
    if v%3==0 and v!=0:
        sum+=v
        count=count+1
		
print("Average:",sum/count)    