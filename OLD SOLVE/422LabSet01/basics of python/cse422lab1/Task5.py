year=int(input("Enter a year:20"))
if year%4==0:
    if year%100==0 and year%400!=0 :
        print("not leap year")
    else:
        print("leap year")
else:
    print("not leap year")
