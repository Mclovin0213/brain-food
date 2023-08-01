testStr = ["eat","tea","tan","ate","nat","bat"]

def groupAnagrams(strs):
    strTable = {}
    
    for str in strs:
        sortedWord = ''.join(sorted(str))
        
        if sortedWord not in strTable:
            strTable[sortedWord] = []
        
        strTable[sortedWord].append(str)
    
    return list(strTable.values())
    

print(groupAnagrams(testStr))

# def groupAnagrams(strs):
#     result = []
#     for i, str in enumerate(strs):
#         sortedWord = ''.join(sorted(str))
#         inserted = False
        
#         if len(result) == 0:
#             result.append([str])
#         else:
#             for group in result:
#                 if sortedWord == ''.join(sorted(group[0])):
#                     group.append(str)
#                     inserted = True
#             if inserted != True:
#                 result.append([str])
    
#     return result