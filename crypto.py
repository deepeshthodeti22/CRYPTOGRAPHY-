def linear_search(arr, target):
    # Scan the array left to right
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Return the index if found
    return -1  # Return -1 if the target is not in the array

# Example usage:
numbers = [10, 50, 30, 70, 80, 20]
print(linear_search(numbers, 30))
print(linear_search(numbers, 99))  
