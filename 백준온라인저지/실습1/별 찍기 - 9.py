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
# 5
# 예제 출력 1
# *********
#  *******
#   *****
#    ***
#     *
#    ***
#   *****
#  *******
# *********

N = int(input())

# 직접 노트에 별을 그려보며 i의 수열을 찾아내라
# N이 넘는다면 분리하라 (이런 방법 밖에 찾을 수 가 없더라.)
# abs() 절대값 함수
for i in range(N):
    for _ in range((N - abs(N - i))):
        print(' ', end = '')
    for _ in range(abs(2 * N - (2 * i + 1))):
        print('*', end = '')
    print()

for i in reversed(range(0, N - 1)):
    for _ in range((N - abs(N - i))):
        print(' ', end = '')
    for _ in range(abs(2 * N - (2 * i + 1))):
        print('*', end = '')
    print()
