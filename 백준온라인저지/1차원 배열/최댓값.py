# 문제
# 9개의 서로 다른 자연수가 주어질 때, 이들 중 최댓값을 찾고 그 최댓값이 몇 번째 수인지를 구하는 프로그램을 작성하시오.
#
# 예를 들어, 서로 다른 9개의 자연수
#
# 3, 29, 38, 12, 57, 74, 40, 85, 61
#
# 이 주어지면, 이들 중 최댓값은 85이고, 이 값은 8번째 수이다.
#
# 입력
# 첫 째 줄부터 아홉 번째 줄까지 한 줄에 하나의 자연수가 주어진다. 주어지는 자연수는 100 보다 작다.
#
# 출력
# 첫째 줄에 최댓값을 출력하고, 둘째 줄에 최댓값이 몇 번째 수인지를 출력한다.
#

# 시간 복잡도가 높은 답안
# numbers = [int(input()) for _ in range(9)]
# MAX = max(numbers)
# count = 0
# while numbers[count] != MAX:
#     count += 1
# # count는 배열의 인덱스 이므로
# print("%d %d" %(MAX, count + 1))

numbers = []
MAX = 0
index = 0
for i in range(9):
    numbers.append(int(input()))
    if numbers[i] > MAX:
        MAX = numbers[i]
        index = i + 1
    else:
        pass
print("%d\n%d" %(MAX, index))