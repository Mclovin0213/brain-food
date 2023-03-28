test_scores = [12, 24, 10, 24]

def breakingRecords(scores):
    min_max_count = [0, 0]
    maximum = scores[0]
    minimum = scores[0]

    for num in scores:
        if num > maximum:
            min_max_count[0] += 1
            maximum = num
        elif num < minimum:
            min_max_count[1] += 1
            minimum = num

    return min_max_count

print(breakingRecords(test_scores))
