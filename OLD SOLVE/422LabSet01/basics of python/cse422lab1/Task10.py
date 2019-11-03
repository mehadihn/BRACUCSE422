import math
a=int(input("Enter value:"))
b=int(input("Enter value:"))
c=int(input("Enter value:"))
s=(a+b+c)/2
area = math.sqrt(s*(s-a)*(s-b)*(s-c))
print ("Area of the triangle is ",area)