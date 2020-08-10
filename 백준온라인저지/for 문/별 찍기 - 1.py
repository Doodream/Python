# 문제
# 첫째 줄에는 별 1개, 둘째 줄에는 별 2개, N번째 줄에는 별 N개를 찍는 문제
#
# 입력
# 첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.
#
# 출력
# 첫째 줄부터 N번째 줄까지 차례대로 별을 출력한다.
#
# 예제 입력 1
# 5
# 예제 출력 1
# *
# **
# ***
# ****
# *****

import sys
N = int(sys.stdin.readline())

for i in range(1, N + 1):
    for j in range(i):
        # print를 여러번 하면서 붙여 출력할 수 있는 방법은  print("~~~", end = '') end는 끝에 어떤 것을 붙여이을 것이냐.
        # print를 한번만 하면서 여러줄 출력 하는 방법 print(1, 2, 3, sep = '\n')
        print('*', end = '')
    print("")
