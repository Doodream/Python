# 동빈이네 전자매장에는 부품이 N개 있다. 각 부품은 정수 형태의 고유한 번호가 있다.
# 어느날 손님이 M개 종류의 부품을 대량으로 구매하겠다며 당일 날 견적서를 요청했다.
# 동빈이는 때를 놓치지 않고 손님이 문의한 부품 M개 종류를 모두 확인해서 견적서를 작성해야 한다.
# 이때 가게 안에서 부품이 모두 있는지 확인하는 프로그램을 작성해보자.
#
# 입력조건
# - 첫째 줄에 정수 N이 주어진다. (1 <= N <= 1000000)
# - 둘째 줄에는 공백으로 구분하여 N개의 정수가 주어진다. 이떄 정수는 1보다 크고 1000000이하이다.
# - 셋째 줄에는 정수 M이 주어진다. (1 <= M <= 100000)
# - 넷째 줄에는 공백으록 구분하여 M개의 정수가 주어진다. 이때 정수는 1보다 크고 10억 이하이다.
#
# 출력조건
# - 첫째 줄에 공백으로 구분하여 각 부품이 존재하면 yes, 없으면  no를 출력한다.
# 이진 탐색으로 구현해보자

# 이진 탐색
def binary_search(arr, var, low, high):
    middle = int((low + high) / 2)

    # low 가 high를 추월하면 더이상 탐색 불가
    if low > high:
        return -1

    if var == arr[middle]:
        return middle
    elif var > arr[middle]:
        return binary_search(arr, var, middle + 1, high)
    elif var < arr[middle]:
        return binary_search(arr, var, low, middle - 1)
    else:
        return -1


N = int(input())
parts = list(map(int, input().split()))
M = int(input())
con_parts = list(map(int, input().split()))
# 부품들을 먼저 정렬을 해놔야 이진탐색이 가능하다.
parts.sort()

# 손님이 요구한 부품 확인
for i in con_parts:
    if binary_search(parts, i, 0, N - 1) == -1:
        print("no")
    else:
        print("yes")





