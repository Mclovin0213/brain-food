testArray = [1, 2, 3, 4, 5]

def miniMaxSum(arr):
    results = []

    for i in range(len(arr)):
        total = 0
        for index, val in enumerate(arr):
            if index == i:
                continue
            total += val

        results.append(total)

    print(f"{min(results)} {max(results)}")

miniMaxSum(testArray)



