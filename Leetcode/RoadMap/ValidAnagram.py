S = "mile"
T = "lime"

def isAnagram(s, t):
    list1 = []
    list2 = []

    for char in s:
        list1.append(char)

    for char in t:
        list2.append(char)

    if sorted(list1) == sorted(list2):
        return True
    else:
        return False

print(isAnagram(S,T))