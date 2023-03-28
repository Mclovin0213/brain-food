testArray = [1, 1, 0, -1, -1]

def plusMinus(arr):
    size = len(arr)
    one_count = 0
    zero_count = 0
    neg_count = 0

    for num in arr:
        if num > 0:
            one_count += 1
        elif num < 0:
            neg_count += 1
        else:
            zero_count += 1

    print("%.6f" % (one_count/size))
    print("%.6f" % (neg_count/size))
    print("%.6f" % (zero_count/size))


plusMinus(testArray)