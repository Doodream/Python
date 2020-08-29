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
graph = []
# 3차원 배열의 [0][0] 부분은 벽을 부순적이 있는가 없는가? 를 추가로 나타내기 위해서
visited = [[[0]*2 for _ in range(M)] for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(N):
    graph.append(list(map(int, input())))


def bfs(x, y, status):
    q = deque()
    q.append((x, y, status))
    visited[x][y][status] = 1
    while q:
        nx, ny, nstatus = q.popleft()
        for i in range(4):
            xx, yy = nx + dx[i], ny + dy[i]
            # 범위가 넘어가지 않았다면
            if 0 <= xx < N and 0 <= yy < M:
                # 방문한 적이 없고 벽이 없는 곳이면
                if visited[xx][yy][nstatus] == 0 and graph[xx][yy] == 0:
                    # 이동 횟수 누적
                    visited[xx][yy][nstatus] = visited[nx][ny][nstatus] + 1
                    q.append((xx, yy, nstatus))
                # 현재 까지 벽이 한번도 부숴진 적이 없다면
                if nstatus == 0:
                # 현재까지 방문한 적이 없고 벽이 있다면
                    if visited[xx][yy][nstatus + 1] == 0 and graph[xx][yy] == 1:
                        # 벽이 부숴진 벽에 최단거리 입력하여 부순 흔적 체크와 최단거리 입력
                        visited[xx][yy][nstatus + 1] = visited[nx][ny][nstatus] + 1
                        # 이후로는 벽이 부숴진 흔적을 큐로 남겨야 하므로 nstatus + 1을 다음 큐에 입력한다.
                        q.append((xx, yy, nstatus + 1))


bfs(0, 0, 0)
# 벽을 부수기 전의 값도 있고 벽을 부순 후의 값도 있다면 둘중 작은 것을 출력
# (벽을 부숴도 갈 수 있고, 굳이 부수지 않더라도 도달 할 수 있다)
if visited[N - 1][M - 1][0] != 0 and visited[N - 1][M - 1][1] != 0:
    print(min(visited[N - 1][M - 1][0], visited[N - 1][M - 1][1]))
# 벽을 부수기 전의 값만 있다(벽을 부수면 도달이 불가능한 경우)
elif visited[N - 1][M - 1][0] != 0:
    print(visited[N - 1][M - 1][0])
# 벽을 부순 후의 값만 있다.(벽을 부숴야지만 도달 가능한 경우)
elif visited[N - 1][M - 1][1] != 0:
    print(visited[N - 1][M - 1][1])
# 둘다 값이 없다면 애초에 도달이 아얘 불가능한 경우
else:
    print(-1)



