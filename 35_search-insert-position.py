# NORMAL
# def searchInsert(nums, target):
#     if target in nums:
#         return nums.index(target)
#     elif target < nums[0]:
#         return 0
#     else:
#         c = nums[0]
#         for i in nums:
#             if i < target:
#                 c = i
#         return nums.index(c) + 1

# OPTIMIZED
def searchInsert(nums, target):
    for i in range(len(nums)):
        print(f'i: {i}')
        if nums[i] >= target:
            print(f'i inner: {i}')
            return i
    return i+1


nums = [1, 3, 5, 6]
target = 5
nums = [1, 3, 5, 6]
target = 0
nums = [2, 5]
target = 3

print(searchInsert(nums, target))
