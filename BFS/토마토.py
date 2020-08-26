# 철수의 토마토 농장에서는 토마토를 보관하는 큰 창고를 가지고 있다.
# 토마토는 아래의 그림과 같이 격자 모양 상자의 칸에 하나씩 넣어서 창고에 보관한다.
#
#
#
# 창고에 보관되는 토마토들 중에는 잘 익은 것도 있지만, 아직 익지 않은 토마토들도 있을 수 있다.
# 보관 후 하루가 지나면, 익은 토마토들의 인접한 곳에 있는 익지 않은 토마토들은 익은 토마토의 영향을 받아 익게 된다.
# 하나의 토마토의 인접한 곳은 왼쪽, 오른쪽, 앞, 뒤 네 방향에 있는 토마토를 의미한다.
# 대각선 방향에 있는 토마토들에게는 영향을 주지 못하며, 토마토가 혼자 저절로 익는 경우는 없다고 가정한다.
# 철수는 창고에 보관된 토마토들이 며칠이 지나면 다 익게 되는지, 그 최소 일수를 알고 싶어 한다.
#
# 토마토를 창고에 보관하는 격자모양의 상자들의 크기와 익은 토마토들과 익지 않은 토마토들의 정보가 주어졌을 때,
# 며칠이 지나면 토마토들이 모두 익는지, 그 최소 일수를 구하는 프로그램을 작성하라.
# 단, 상자의 일부 칸에는 토마토가 들어있지 않을 수도 있다.
#
# 입력
# 첫 줄에는 상자의 크기를 나타내는 두 정수 M,N이 주어진다. M은 상자의 가로 칸의 수, N은 상자의 세로 칸의 수를 나타낸다.
# 단, 2 ≤ M,N ≤ 1,000 이다. 둘째 줄부터는 하나의 상자에 저장된 토마토들의 정보가 주어진다.
# 즉, 둘째 줄부터 N개의 줄에는 상자에 담긴 토마토의 정보가 주어진다.
# 하나의 줄에는 상자 가로줄에 들어있는 토마토의 상태가 M개의 정수로 주어진다.
# 정수 1은 익은 토마토, 정수 0은 익지 않은 토마토, 정수 -1은 토마토가 들어있지 않은 칸을 나타낸다.
#
# 출력
# 여러분은 토마토가 모두 익을 때까지의 최소 날짜를 출력해야 한다.
# 만약, 저장될 때부터 모든 토마토가 익어있는 상태이면 0을 출력해야 하고,
# 토마토가 모두 익지는 못하는 상황이면 -1을 출력해야 한다.
from collections import deque

M, N = map(int, input().split())
graph = []
# 그래프의 익은 토마토 위치 딸 리스트
ripe_tomatos = []
# 인접 노드 방향
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
# 안익은 토마토 갯수
underripe_tomatos = 0
# bfs이후 안익은 토마토 갯수
after_bfs_tomatos = 0
answer = 0

for i in range(N):
    graph.append(list(map(int, input().split())))

# 익은 토마토 위치 따서 리스트에 넣기
for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            ripe_tomatos.append([i, j])

# 이문제는 queue를 이용하여 처음에 여러 노드를 queue에 집에 넣고 시작해야 되기 때문에
# 탐색시 queue를 이용하는 bfs를 이용한다.

def bfs(tomatos):
    queue = deque()
    # 익은 토마토의 위치를 큐에 넣기
    for i in tomatos:
        xx = i[0]
        yy = i[1]
        queue.append((xx, yy))
    # bfs 탐색시작
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx > N - 1 or ny < 0 or ny > M - 1:
                continue
            if graph[nx][ny] == 0:
                queue.append((nx, ny))
                # 인접 토마토가 아직 익지 않았다면 날짜수 누적
                graph[nx][ny] = graph[x][y] + 1
    # 마지막으로 큐에서 나오는 토마토가 익은 날짜 수 출력
    return graph[x][y]

# bfs 하기전 안익은 토마토의 갯수를 세고
for i in range(N):
    underripe_tomatos += graph[i].count(0)

# bfs 탐색
answer = bfs(ripe_tomatos)

# bfs 한 후 안익은 토마토 갯수를 세고
for i in range(N):
    after_bfs_tomatos += graph[i].count(0)

# bfs 하기전 안익은 토마토의 갯수가 없다면 (모두 익었다는 뜻이므로)
if underripe_tomatos == 0:
    print(0)
# bfs 한 후 안익은 토마토의 갯수가 하나라도 있다면 (토마토가 모두 익을 수 없는 환경이란 의미 이므로)
elif after_bfs_tomatos != 0:
    print(-1)
# 그렇지 않은 일반적인 경우
else:
    # 처음부터 토마토가 익은 날짜수는 제외
    print(answer - 1)
