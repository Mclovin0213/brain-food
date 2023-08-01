testNums = [2,7,11,15]
testTarget = 9

def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]

# ! O(N) method
# def twoSum(nums, target):
#     d = {}
#     for i, j in enumerate(nums):
#         r = target - j
#         if r in d: return [d[r], i]
#         d[j] = i