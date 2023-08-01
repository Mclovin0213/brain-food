nums = [1,1,1,2,2,3,3,3,3,3]
k = 2

def topKFrequent(nums, k):
    numCounts = {}
    result = []
    for num in nums:
        if num in numCounts.keys():
            numCounts[num] = numCounts[num] + 1
        else:
            numCounts[num] = 1
    for _ in range(k):
        maxNum = max(numCounts, key=numCounts.get)
        result.insert(1, maxNum)
        numCounts.pop(maxNum)
    return result

print(topKFrequent(nums, k))
