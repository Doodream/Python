# 문제
# 두 자연수 A와 B가 있을 때, A%B는 A를 B로 나눈 나머지 이다. 예를 들어, 7, 14, 27, 38을 3으로 나눈 나머지는 1, 2, 0, 2이다.
#
# 수 10개를 입력받은 뒤, 이를 42로 나눈 나머지를 구한다. 그 다음 서로 다른 값이 몇 개 있는지 출력하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄부터 열번째 줄 까지 숫자가 한 줄에 하나씩 주어진다. 이 숫자는 1,000보다 작거나 같고, 음이 아닌 정수이다.
#
# 출력
# 첫째 줄에, 42로 나누었을 때, 서로 다른 나머지가 몇 개 있는지 출력한다.
#
# 예제 입력 1
# 39
# 40
# 41
# 42
# 43
# 44
# 82
# 83
# 84
# 85
# 예제 출력 1
# 6

numbers = [int(input()) for _ in range(10)]
# lambda 인수값 : return 값
rest_numbers = list(map(lambda x : x % 42, numbers))
# 인덱스 여러개 찾기
# filter 함수 : list(filter(func, list[]))
# generator expression : [i for i in list[] func]

# 해답 1
# 나머지 숫자들중에
# for i in rest_numbers:
#     count = 0
#     # 한 원소가 2개 이상있다면 해당원소를 double_index 배열에 포함
#     for j in range(len(rest_numbers)):
#         if rest_numbers[j] == i:
#             count += 1
#         else:
#             pass
#
#     if count > 1:
#         # 원소가 2개 이상이면 제거하여 중복되지 않게 만들어버린다.
#         rest_numbers.remove(i)
#         # print(rest_numbers)
#
# print(len(rest_numbers))

# 해답 2 set은 중복된 원소를 제거하고 집합으로 만든다.
rest_numbers = set(rest_numbers)
print(len(rest_numbers))

