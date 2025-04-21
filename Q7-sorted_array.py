def find_common_elements(arr1, arr2):
    i = 0
    j = 0
    result = []
    prev = None

    while i < len(arr1) and j < len(arr2):
        if arr1[i] == arr2[j]:
            if arr1[i] != prev:  
                result.append(arr1[i])
                prev = arr1[i]
            i += 1
            j += 1
        elif arr1[i] < arr2[j]:
            i += 1
        else:
            j += 1

    return result


# given array number
arr1 = [1, 2, 2, 3, 4, 5]
arr2 = [2, 2, 3, 5, 6]

common = find_common_elements(arr1, arr2)
print("Common elements:", common)
