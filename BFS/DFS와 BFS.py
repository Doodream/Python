# 문제
# 그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오.
# 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고,
# 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.
#
# 입력
# 첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000),
# 탐색을 시작할 정점의 번호 V가 주어진다. 다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다.
# 어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 입력으로 주어지는 간선은 양방향이다.
#
# 출력
# 첫째 줄에 DFS를 수행한 결과를, 그 다음 줄에는 BFS를 수행한 결과를 출력한다. V부터 방문된 점을 순서대로 출력하면 된다.
from collections import deque

def print_graph():
    for i in range(len(graph)):
        print(graph[i])
    print()


def dfs(v):
    # 방문처리
    visited[v] = 1
    # 방문출력
    print(v, end=' ')
    # 그래프에 연결되어 있는 노드들
    for i in graph[v]:
        # 방문이 안되었다면
        if visited[i] == 0:
            # 재귀
            dfs(i)


def bfs(v):
    # 큐 생성
    queue = deque()
    queue.append(v)
    # 방문 처리
    visited[v] = 1
    # 방문 출력
    print(v, end = ' ')

    # 큐가 비워질 때 까지
    while queue:
        # 큐에서 꺼내서
        x = queue.popleft()
        # 연결된 노드들을 모두 돌면서
        for i in graph[x]:
            # 방문하지 않았다면
            if visited[i] == 0:
                # 방문처리
                visited[i] = 1
                # 큐에 넣는다.
                queue.append(i)
                # 방문 출력
                print(i, end = ' ')


N, M, V = map(int, input().split())
edge = []
for _ in range(M):
    edge.append(list(map(int, input().split())))

graph = [[] for _ in range(N + 1)]

for e in edge:
    graph[e[0]].append(e[1])
    graph[e[1]].append(e[0])

for i in graph:
    i.sort()

visited = [0] * (N + 1)
stack = []

dfs(V)
print()
visited = [0] * (N + 1)
bfs(V)
