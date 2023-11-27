def find_max(arr):

    if len(arr) == 0:
        return None

    max_index = 0

    for i in range(len(arr)):
        if (arr[i] > max_index):
            max_index = arr[i]
    return max_index

result = find_max([5, 54, 5, 47, 54, 54, 55, 4, 57, 54, 58, 48, 75])
print(result)
