li = [2, 6, 11, 13, 18, 20, 22, 27, 29, 30, 34, 38, 41, 42, 45, 47]

def binary_search(arr, var, low, high):
    middle = int((low + high) / 2)
    if var == arr[middle]:
        return middle
    elif var < arr[middle]:
        # 재귀함수는 맨끝에 있는 것을 반환해야 맨 앞의 재귀함수까지 반환된다.
        return binary_search(arr, var, low, middle - 1)
    elif var > arr[middle]:
        return binary_search(arr, var, middle + 1, high)
    else:
        print("Cant search value")

print(binary_search(li, 22, 0, len(li) - 1))

