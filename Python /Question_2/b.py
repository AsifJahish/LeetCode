def find_indices(arr, target):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == target:
                return i, j  # Return the indices of the two numbers
    return None  # Return None if no solution is found

# Example usage:
arr1 = [2, 7, 11, 15]
target2 = 9
result = find_indices(arr1, target2)
print(result)  # Output: (0, 1)

