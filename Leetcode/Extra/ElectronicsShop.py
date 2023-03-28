budget = 10
k = [1, 2]
d = [5, 2, 7]

def getMoneySpent(keyboards, drives, b):
    results = []
    for board in keyboards:
        total = 0
        total += board

        if total > b:
            continue

        b_total = total

        for drive in drives:
            total = b_total
            total += drive

            if total > b:
                continue
            else:
                results.append(total)

    if len(results) == 0:
        return -1

    final = 0

    for result in results:
        if result > final:
            final = result

    return final


print(getMoneySpent(k, d, budget))