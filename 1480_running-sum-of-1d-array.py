nums = [1, 2, 3, 4]
# nums = [1,1,1,1,1]
# nums = [3, 1, 2, 10, 1]


counter = nums[0]
for i in range(1, len(nums)):
    # nums[i] = nums[i] + counter
    # counter = nums[i]
    nums[i] += nums[i-1]

print(nums)
