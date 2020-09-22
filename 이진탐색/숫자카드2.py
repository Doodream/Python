# 문제
# 숫자 카드는 정수 하나가 적혀져 있는 카드이다. 상근이는 숫자 카드 N개를 가지고 있다.
# 정수 M개가 주어졌을 때, 이 수가 적혀있는 숫자 카드를 상근이가 몇 개 가지고 있는지 구하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 상근이가 가지고 있는 숫자 카드의 개수 N(1 ≤ N ≤ 500,000)이 주어진다.
# 둘째 줄에는 숫자 카드에 적혀있는 정수가 주어진다.
# 숫자 카드에 적혀있는 수는 -10,000,000보다 크거나 같고, 10,000,000보다 작거나 같다.
#
# 셋째 줄에는 M(1 ≤ M ≤ 500,000)이 주어진다.
# 넷째 줄에는 상근이가 몇 개 가지고 있는 숫자 카드인지 구해야 할 M개의 정수가 주어지며,
# 이 수는 공백으로 구분되어져 있다. 이 수도 -10,000,000보다 크거나 같고, 10,000,000보다 작거나 같다.
#
# 출력
# 첫째 줄에 입력으로 주어진 M개의 수에 대해서,
# 각 수가 적힌 숫자 카드를 상근이가 몇 개 가지고 있는지를 공백으로 구분해 출력한다.
#
# 예제 입력 1
# 10
# 6 3 2 10 10 10 -10 -10 7 3
# 8
# 10 9 -5 2 3 4 5 -10

# 예제 출력 1
# 3 0 0 1 2 0 0 2


N = int(input())
check_nums = list(map(int, input().split()))
check_nums.sort()
M = int(input())
card_nums = list(map(int, input().split()))
answer = []


def binary_search(arr, var, low, high):
    if low > high:
        return 0
    middle = (low + high) // 2
    if var == arr[middle]:
        return arr[low:high+1].count(var)
    elif var > arr[middle]:
        return binary_search(arr, var, middle + 1, high)
    else:
        return binary_search(arr, var, low, middle - 1)

    # while low <= high:
    #     middle = (low + high) // 2
    #     if var == arr[middle]:
    #         print(arr[low:high+1].count(var), end = ' ')
    #         break
    #     elif var > arr[middle]:
    #         low = middle + 1
    #         if low > high:
    #             print(0, end=' ')
    #             break
    #     elif var < arr[middle]:
    #         high = middle - 1
    #         if low > high:
    #             print(0, end=' ')
    #             break
    #     else:
    #         print(0, end=' ')
    #         break


for i in card_nums:
    print(binary_search(check_nums, i, 0, len(check_nums) - 1), end=' ')



