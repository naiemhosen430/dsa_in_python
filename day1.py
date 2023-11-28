def find_max(arr):

    if len(arr) == 0:
        return None

    max_value = arr[0]

    for i in range(1, len(arr)):
        if (arr[i] > max_value):
            max_value = arr[i]
    return max_value

result = find_max([-5, -54, -5, -47, -6, -54, -54, -54, -55,])
print(result)
