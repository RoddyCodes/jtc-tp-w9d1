def bubble_sort(arr):
    x = len(arr)
    for i in range(x):
        for j in range(0, x-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

#sample cases

array1 = [100, 77, 25, 33, 50, 32, 198]
sorted_array1 = bubble_sort(array1)
print(sorted_array1) #output [32,33,50,77,100,198]