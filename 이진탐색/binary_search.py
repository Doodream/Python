li = [2, 6, 11, 13, 18, 20, 22, 27, 29, 30, 34, 38, 41, 42, 45, 47]

def binary_search(arr, var):
    low = 0
    high = len(arr) - 1
    while low <= high:
        middle = int((low + high)/2)
        if var == arr[middle]:
            return middle
        elif var > arr[middle]:
            low = middle + 1
        elif var < arr[middle]:
            high = middle - 1
        else:
            return "Cant search value"

print(binary_search(li, 22))

