def first_duplicate(arr) :
    seen = set()
    duplicates = -1
    for i in range(len(arr)):
        if arr[i] in seen:
            return arr[i]
        else:
            seen.add(arr[i])
    return duplicates

print(first_duplicate([2, 1, 3, 5, 3, 2]))
print(first_duplicate([1, 2, 3, 4, 4, 5]))
