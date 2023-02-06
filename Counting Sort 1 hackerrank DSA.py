def countingSort(arr):
    count = [0] * 100
    for i in arr:
        count[i] += 1
    return count
