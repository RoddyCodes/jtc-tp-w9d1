def linear_search(arr, target):
    #iterate over each element in array 
    for i in range (len(arr)):
        #checks for element is equal to target value
        if arr[i] == target:
            return i 
    return -1

#sample test cases
array = [10, 23, 45, 70, 11, 15]

target = 70
print(f"Index of {target}: {linear_search(array, target)}")  # Output: 3

target = 11
print(f"Index of {target}: {linear_search(array, target)}")  # Output: 4

target = 99
print(f"Index of {target}: {linear_search(array, target)}")  # Output: -1


