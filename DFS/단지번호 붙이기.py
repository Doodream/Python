# 문제
# <그림 1>과 같이 정사각형 모양의 지도가 있다. 1은 집이 있는 곳을, 0은 집이 없는 곳을 나타낸다.
# 철수는 이 지도를 가지고 연결된 집들의 모임인 단지를 정의하고, 단지에 번호를 붙이려 한다.
# 여기서 연결되었다는 것은 어떤 집이 좌우, 혹은 아래위로 다른 집이 있는 경우를 말한다.
# 대각선상에 집이 있는 경우는 연결된 것이 아니다. <그림 2>는 <그림 1>을 단지별로 번호를 붙인 것이다.
# 지도를 입력하여 단지수를 출력하고, 각 단지에 속하는 집의 수를 오름차순으로 정렬하여 출력하는 프로그램을 작성하시오.
#
# 입력
# 첫 번째 줄에는 지도의 크기 N(정사각형이므로 가로와 세로의 크기는 같으며 5≤N≤25)이 입력되고,
# 그 다음 N줄에는 각각 N개의 자료(0혹은 1)가 입력된다.
#
# 출력
# 첫 번째 줄에는 총 단지수를 출력하시오. 그리고 각 단지내 집의 수를 오름차순으로 정렬하여 한 줄에 하나씩 출력하시오.

N = int(input())
graph = []
village_list = []
for _ in range(N):
    graph.append(list(map(int, input())))
# 전역변수 처리
global village_num
village_num = 0

def dfs(x, y):
    # 함수 내에서도 전역변수 처리
    global village_num
    # 맵사이즈를 넘어간다면 바로 종료(재귀 종료 조건)
    if x < 0 or x > N - 1 or y < 0 or y > N - 1:
        return False
    # 맵이 주택단지라면
    if graph[x][y] == 1:
        graph[x][y] = 0
        village_num += 1
        # 상하좌우 붙어있어야 연결되어 있는 것이므로
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)
        # 모두 연결되어 있다면 (재귀 종료 조건)
        return True
    #  맵이 주택단지가 아니라면 종료(재귀 종료 조건)
    return False

for i in range(N):
    for j in range(N):
        if dfs(i, j) == True:
            village_list.append(village_num)
            village_num = 0

print(len(village_list))
village_list.sort()
for i in village_list:
    print(i)