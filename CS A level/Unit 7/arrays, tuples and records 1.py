numbers = [None] * 6 #creating a blank array called "names" filled with "none" in the values (list treated as an array)
print(numbers)
total = 0
for i in range(len(numbers)):
    numbers[i] = int(input("enter a number"))
    total = total + numbers[i]
    print("the running total of the numbers is ", total)
print(numbers.reverse)
avg = total/len(numbers)
print("the final total of the numbers is ", total)
print("the average of the numbers is ", avg, "which can be rounded to ", int(avg))