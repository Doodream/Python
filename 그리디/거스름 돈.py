# 예제 3 - 1 거스름돈
#
#
# 당신은 음식점의 계산을 도와주는 점원이다.
# 카운터에는 거스름돈으로 사용할 500원, 100원, 50원, 10원 짜리 동전이 무한히 존재한다고 가정한다.
# 손님에게 거슬러 줘야 할 돈이 N원일 때 거슬러 줘야 할 동전의 최소 개수를 구해라.
# 단 거슬러 줘야 할 돈 N은 항상 10의 배수이다.

import sys

N = int(sys.stdin.readline())

count = 0
list = [500, 100, 50, 10]
# 큰 수 부터 차례대로 걸러야 함.
list.sort(reverse = True)

for coin in list:
    # 코인을 큰 수부터 나눈 나머지를 다음 작은 코인들로 나눠야함.
    count += N // coin
    N = N % coin

print(count)