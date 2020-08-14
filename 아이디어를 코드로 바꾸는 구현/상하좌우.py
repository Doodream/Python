# 여행가 A는 N * N 크기의 정사각형 공간 위에 서있다. 이공간은 1 * 1 크기의 정사각형으로 나누어져 있다.
# 가장 왼쪽 위 좌표는 (1, 1)이며 가장 오른 쪽 아래 좌표는 (N, N)에 해당한다. 여행가 A는 상, 하 ,좌 ,우 방향으로 이동할 수 있으며
# 시작좌표는 항상(1, 1)이다. 우리앞에는 여행가가 A가 이동할 계획서가 놓여있다.
# 계획서에는 하나의 줄에 띄어쓰기를 기준으로 하여 L, R, U, D중 하나의 문자가 반복적으로 적혀 있다. 각 문자의 의미는
# 다음과 같다.
#
# L : 왼쪽으로 한 칸 이동
# R : 오른쪽으로 한 칸 이동
# U : 위로 한 칸 이동
# D : 아래로 한 칸 이동
#
# 이때 여행가 A가 N * N 크기의 정사각형 공간을 벗어나는 움직임은 무시된다. 예를 들어 (1, 1) 의 위치에서 L 혹은 U를 만나면
# 무시된다.  계획서가 주어졌을 때 여행가 A가 최종적으로 도착할 지점의 좌표를 출력하는 프로그램을 작성하시오.
#
# 입력조건
# - 첫째 줄에 공간의 크기를 나타내는 N이 주어진다.
# - 둘째 줄에 여행가 A가 이동할 계획서의 내용이 주어진다.
#
# 출력조건
# - 첫째 줄에 여행가 A가 최종적으로 도착할 지점의 좌표 (X, Y)를 공백으로 구분하여 출력한다.

def L(location):
    location[1] -= 1
    return location

def R(location):
    location[1] += 1
    return location

def U(location):
    location[0] -= 1
    return location


def D(location):
    location[0] += 1
    return location

N = int(input())
plan = list(map(str, input().split()))
location = [1, 1]

for i in plan:

    if i == 'L':
       location = L(location)
       # 공간을 넘어가는 경우 원복
       if 0 in location:
           location = R(location)
    elif i == 'R':
       location = R(location)
       if 0 in location:
           location = L(location)
    elif i == 'U':
       location = U(location)
       if 0 in location:
           location = D(location)
    else:
        location = D(location)
        if 0 in location:
            location = U(location)

print(location)

