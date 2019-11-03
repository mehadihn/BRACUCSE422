import math
value1=int(input("Enter value:"))
value2=int(input("Enter value:"))
value3=int(input("Enter value:"))
s=(value1+value2+value3)/2
area = math.sqrt(s*(s-value1)*(s-value2)*(s-value3))
print ("Area of the triangle is ",area)