nums = [2, 5, 4, 7, 8, "teehee", 6, 7]
print(nums)
nums.pop()
print(nums.pop())
nums.append(10)
print(nums)
for each in nums:
    print(each, end=" ")

print()

for i in range(len(nums)):
    print(nums[i])