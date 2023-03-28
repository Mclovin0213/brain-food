testNums = [1, 2, 3, 1]

def containsDuplicate(self, nums):
    numSet = set()
    for num in nums:
        if num in numSet:
            return True
        else:
            numSet.add(num)
    return False