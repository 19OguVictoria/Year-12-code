numbers = [3,6,2,8,1]
def addNums(numbers):
    print("At function call (inside): ", numbers)
    if len(numbers) == 1:
        print("Base Case reached: ", numbers)
        return numbers[0]
    else:
        print("next function call: ", numbers[1:])
        return numbers[0] + addNums(numbers[1:])

marks = [3,6,2,8,1]
total = addNums(marks)
print(total)



