for value in range (5):
    value = input("Input 6 number :")
    numbers = list(map(int, value.split()))
    length = len(numbers)
    numbers.sort()
    print("Sum of smallest and largest number is:", numbers[length-1]+numbers[0])
    print("Sum of second smallest and second largest number is:", numbers[length-2]+numbers[1])
    print("Sum of third smallest and third largest number is:", numbers[length-3]+numbers[2])
