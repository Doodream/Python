# 문제
# N×M크기의 배열로 표현되는 미로가 있다.
#
# 1	 0	1	1	1	1
# 1	 0	1	0	1	0
# 1	 0	1	0	1	1
# 1	 1	1	0	1	1
# 미로에서 1은 이동할 수 있는 칸을 나타내고, 0은 이동할 수 없는 칸을 나타낸다.
# 이러한 미로가 주어졌을 때, (1, 1)에서 출발하여
# (N, M)의 위치로 이동할 때 지나야 하는 최소의 칸 수를 구하는 프로그램을 작성하시오.
# 한 칸에서 다른 칸으로 이동할 때, 서로 인접한 칸으로만 이동할 수 있다.
#
# 위의 예에서는 15칸을 지나야 (N, M)의 위치로 이동할 수 있다. 칸을 셀 때에는 시작 위치와 도착 위치도 포함한다.
#
# 입력
# 첫째 줄에 두 정수 N, M(2 ≤ N, M ≤ 100)이 주어진다. 다음 N개의 줄에는 M개의 정수로 미로가 주어진다.
# 각각의 수들은 붙어서 입력으로 주어진다.
#
# 출력
# 첫째 줄에 지나야 하는 최소의 칸 수를 출력한다. 항상 도착위치로 이동할 수 있는 경우만 입력으로 주어진다.
from _collections import deque

N, M = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, input())))

# 인접한 노드를 판별하기 위한 방향
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    # 큐 생성
    queue = deque()
    # 큐에 시작 노드 넣기
    queue.append((x, y))

    # 큐에 아무것도 없을 때 까지
    while queue:
        # 큐에서 가장 먼저들어온 노드 빼기
        x, y = queue.popleft()

        # 4가지 방향 돌악보기
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 맵의 크기를 넘으면 무시
            if nx < 0 or nx > N - 1 or ny < 0 or ny > M - 1:
                continue
            # 인접하다면
            if graph[nx][ny] == 1:
                # 큐에 노드를 넣고
                queue.append((nx, ny))
                # 노드를 처음 방문한다면 최단 거리 축적
                graph[nx][ny] = graph[x][y] + 1
    # 가장 끝의 출구의 노드의 최단거리 출력
    return graph[N - 1][M - 1]

print(bfs(0, 0))
