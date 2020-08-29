# N×M의 행렬로 표현되는 맵이 있다. 맵에서 0은 이동할 수 있는 곳을 나타내고, 1은 이동할 수 없는 벽이 있는 곳을 나타낸다.
# 당신은 (1, 1)에서 (N, M)의 위치까지 이동하려 하는데, 이때 최단 경로로 이동하려 한다.
# 최단경로는 맵에서 가장 적은 개수의 칸을 지나는 경로를 말하는데, 이때 시작하는 칸과 끝나는 칸도 포함해서 센다.
#
# 만약에 이동하는 도중에 한 개의 벽을 부수고 이동하는 것이 좀 더 경로가 짧아진다면, 벽을 한 개 까지 부수고 이동하여도 된다.
#
# 맵이 주어졌을 때, 최단 경로를 구해 내는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 N(1 ≤ N ≤ 1,000), M(1 ≤ M ≤ 1,000)이 주어진다.
# 다음 N개의 줄에 M개의 숫자로 맵이 주어진다. (1, 1)과 (N, M)은 항상 0이라고 가정하자.
#
# 출력
# 첫째 줄에 최단 거리를 출력한다. 불가능할 때는 -1을 출력한다.
from collections import deque

N, M = map(int, input().split())
graph = [list(map(int, input())) for _ in range(N)]
distance = [[[0]*2 for _ in range(M)] for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, status):
    q = deque()
    q.append((x, y, status))
    distance[x][y][status] = 1

    while q:
        cx, cy, status = q.popleft()
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if graph[nx][ny] == 0 and distance[nx][ny][status] == 0:
                    distance[nx][ny][status] = distance[cx][cy][status] + 1
                    q.append((nx, ny, status))
                # 현재 이미 벽을 부수지 않은 상태이므로 당연히 distance[nx][ny][status + 1] == 0 이다.
                if status == 0:
                    if graph[nx][ny] == 1:
                        distance[nx][ny][status + 1] = distance[cx][cy][status] + 1
                        q.append((nx, ny, status + 1))


bfs(0, 0, 0)

if distance[N - 1][M - 1][0] != 0 and distance[N - 1][M - 1][1] != 0:
    print(min(distance[N - 1][M - 1]))
elif distance[N - 1][M - 1][0] != 0:
    print(distance[N - 1][M - 1][0])
elif distance[N - 1][M - 1][1] != 0:
    print(distance[N - 1][M - 1][1])
else:
    print(-1)