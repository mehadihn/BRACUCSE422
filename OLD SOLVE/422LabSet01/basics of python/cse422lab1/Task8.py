for x in range (5):
    x = input("Input 6 number :")
    numbers = list(map(int, x.split()))
    length = len(numbers)
    numbers.sort()
    print("Sum of the smallest and largest number is:", numbers[length-1]+numbers[0])
    print("Sum of the second smallest and second largest number is:", numbers[length-2]+numbers[1])
    print("Sum of the third smallest and third largest number is:", numbers[length-3]+numbers[2])
