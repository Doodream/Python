# 0 또는 양의 정수가 주어졌을 때, 정수를 이어 붙여 만들 수 있는 가장 큰 수를 알아내 주세요.
#
# 예를 들어, 주어진 정수가 [6, 10, 2]라면 [6102, 6210, 1062, 1026, 2610, 2106]를 만들 수 있고, 이중 가장 큰 수는 6210입니다.
#
# 0 또는 양의 정수가 담긴 배열 numbers가 매개변수로 주어질 때, 순서를 재배치하여 만들 수 있는 가장 큰 수를 문자열로 바꾸어 return 하도록 solution 함수를 작성해주세요.
#
# 제한 사항
# numbers의 길이는 1 이상 100,000 이하입니다.
# numbers의 원소는 0 이상 1,000 이하입니다.
# 정답이 너무 클 수 있으니 문자열로 바꾸어 return 합니다.
# 입출력 예
# numbers	return
# [6, 10, 2]	6210
# [3, 30, 34, 5, 9]	9534330

def quicksort(arr):
    if len(arr) < 2:
        return arr
    pivot = arr[0]
    less = [i for i in arr[1:] if i + pivot >= pivot + i]
    greater = [i for i in arr[1:] if i + pivot < pivot + i]
    arr = quicksort(less) + [pivot] + quicksort(greater)

    return arr

def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(reverse = True)

    quicksort(numbers)
    # count = 0
    # while count < len(numbers)/2:
    #     for i in range(0, len(numbers)-1):
    #         if numbers[i] + numbers[i + 1] > numbers[i + 1] + numbers[i]:
    #             continue
    #         else:
    #             temp = numbers[i]
    #             numbers[i] = numbers[i + 1]
    #             numbers[i + 1] = temp
    #     count = count + 1

    numbers = ''.join(numbers)
    numbers = int(numbers)
    numbers = str(numbers)
    return numbers


numbers2 = [3, 30, 34, 5, 9]
print(solution(numbers2))