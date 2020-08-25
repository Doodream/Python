# 동빈이는 N * M 크기의 직사각형 형태의 미로에 갇혀 있다.
# 미로에는 여러 마리의 괴물이 있어 이를피해 탈출해야한다.
# 동빈이의 위치는 (1, 1)이고 미로의 출구는 (N, M)의 위치에 존재하며 한 번에 한 칸씩 이동할 수 있다.
# 이때 괴물이 있는 부분은 0으로, 괴물이 없는 부분은 1로 표시되어 있다.
# 미로는 반드시 탈출할 수 있는 형태로 제시된다. 이때 동빈이가 탈출하기 위해 움직여야 하는 최소 칸의 개수를 구하시오.
# 칸을 셀 떄는 시작 칸과 마지막 칸을 모두 포함해서 계산한다.
#
# 입력조건
# - 첫째 줄에 두 정수 N, M(4 <= N, M <= 200)이 주어집니다.
# 다음 N개의 줄에는 각각 M개의 정수(0혹은 1)로 미로의 정보가 주어진다.
# 각각의 수들은 공백 없이붙어서 입력으로 제시된다. 또한 시작 칸과 마지막 칸은 항상 1이다.
#
# 출력조건
# - 첫째 줄에 최소 이동 칸의 개수를 출력한다.
from _collections import deque

# 입력
N, M = map(int, input().split())
graph = []
for i in range(N):
    graph.append((list(map(int, input()))))
# 방문 노드 확인
visited = [[False for _ in range(M)] for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
# 거리 확인
answer = [[0 for _ in range(M)] for _ in range(N)]

# 너비 우선 탐색
def bfs(x, y):
    # 큐 생성
    queue = deque()
    # 큐에 노드 삽입
    queue.append((x, y))
    # 방문 처리
    visited[x][y] = True
    # 방문하는 곳에 따라 거리 대입
    answer[x][y] = 1

    # 큐가 비워질 때 까지
    while queue:
        # 큐에서 선입선출
        x, y = queue.popleft()

        # 4가지 방향 대입
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 맵의 범위를 넘어간 경우 무시
            if nx < 0 or nx > N - 1 or ny < 0 or ny > M - 1:
                continue
            # 괴물이 없고 방문표시가 False 인 경우에만
            if graph[nx][ny] == 1 and not visited[nx][ny]:
                # 최단 거리 상승
                # 방문노드를 큐에 삽입
                queue.append((nx, ny))
                # 새로 방문한 노드라면 거리 1 축적
                answer[nx][ny] = answer[x][y] + 1
                # 방문처리
            visited[nx][ny] = True


bfs(0, 0)
print(answer[N - 1][M - 1])
