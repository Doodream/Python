# 문제
# 예제를 보고 규칙을 유추한 뒤에 별을 찍어 보세요.
#
# 입력
# 첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.
#
# 출력
# 첫째 줄부터 2×N-1번째 줄까지 차례대로 별을 출력한다.
#
# 예제 입력 1
# 3
# 예제 출력 1
# *
# **
# ***
# **
# *

import sys

N = int(sys.stdin.readline())
count = 0

# 1번째 줄부터 N번째 줄까지는 일반적인 별찍기
for _ in range(N):
    for _ in range(count + 1):
        print('*', end = '')
    count += 1
    print()

# N + 1번째 부터 역순 별찍기
for _ in range((N - 1)):
    # reversed((range(N)) or range(N, 0, -1) 10부터 1까지 역순 반복
    for _ in reversed(range(count - 1)):
        print('*', end = '')
    count -= 1
    print()
