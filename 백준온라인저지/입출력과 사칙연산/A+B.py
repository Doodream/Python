# 문제1
# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 A와 B가 주어진다. (0 < A, B < 10)
#
# 출력
# 첫째 줄에 A+B를 출력한다.

# 입력 받을 때 여러문자를 공백을 이용하여 입력받고 싶을 때에는 a, b, c ... = input.split()를 이용

# a, b = input().split()
# a = int(a)
# b = int(b)
# print(a - b)

# map함수를 이용하여 int형 형변환을 한줄로!
# input()자체가 반환형이 문자열이므로 .split()함수 적용가능
# a, b = map(int, input().split())
# print(a+b)

# 문제2
# 두 자연수 A와 B가 주어진다. 이때, A+B, A-B, A*B, A/B(몫), A%B(나머지)를 출력하는 프로그램을 작성하시오.
#
# 입력
# 두 자연수 A와 B가 주어진다. (1 ≤ A, B ≤ 10,000)
#
# 출력
# 첫째 줄에 A+B, 둘째 줄에 A-B, 셋째 줄에 A*B, 넷째 줄에 A/B, 다섯째 줄에 A%B를 출력한다.

# a, b = map(int, input().split())
# print(a + b)

a, b = map(int, input().split())
print(a + b)
print(a - b)
print(a * b)
# 몫을 구하는 것이므로 int로 정수만 구함
# 실제 내림을 하려면 from math import floor
# 실제 올림을 하려면 from math import ceil
print(int(a / b))
print(a % b)
