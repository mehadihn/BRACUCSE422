def fact(n):
    if n == 1:
        return 1
    
    return n*fact(n-1)

boolean = True
n = 1
while(boolean):
    f = str(fact(n))
    #print(f)
    f1 = str(f)
    sum = 0
    for i in range (len(f1)):
        sum = sum + int(f[i])
        #print(sum)
    if (int(f)%sum == 0):
        #print ("Yes")
        n = n+1
    else:
        print("smallest positive integer, n, whose factorial is not divisible by the sum of its digits is",n)
        boolean = False
            
