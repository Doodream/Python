# 수빈이는 동생과 숨바꼭질을 하고 있다. 수빈이는 현재 점 N(0 ≤ N ≤ 100,000)에 있고, 동생은 점 K(0 ≤ K ≤ 100,000)에 있다.
# 수빈이는 걷거나 순간이동을 할 수 있다. 만약, 수빈이의 위치가 X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동하게 된다.
# 순간이동을 하는 경우에는 1초 후에 2*X의 위치로 이동하게 된다.
#
# 수빈이와 동생의 위치가 주어졌을 때, 수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지 구하는 프로그램을 작성하시오.
#
# 입력
# 첫 번째 줄에 수빈이가 있는 위치 N과 동생이 있는 위치 K가 주어진다. N과 K는 정수이다.
#
# 출력
# 수빈이가 동생을 찾는 가장 빠른 시간을 출력한다.
#
# 예제 입력 1
# 5 17
# 예제 출력 1
# 4
from collections import deque

# 그래프 자체가 0부터 100000번째 까지 존재해야하므로
max_size = 100001
N, K = map(int, input().split())
visited = [0 for _ in range(max_size)]

def bfs(node):
    queue = deque()
    queue.append(node)
    # 노드를 방문하였으므로
    visited[node] = 1

    while queue:
        current = queue.popleft()
        # 인접노드를 설정하자
        d = [current - 1, current + 1, current * 2]
        # 술래를 잡는 다면
        if current == K:
            return visited[current] - 1
        # 인접노드를 돌자
        for i in d:
            next = i
            # 다음 칸이 범위 내에 있고 방문하지 않은 칸이라면
            if (0 <= next < max_size) and (visited[next] == 0):
                # 해당 칸에 현재 시간을 적어놓자
                visited[next] = visited[current] + 1
                queue.append(next)

#
if N > K:
    print(N - K)
elif N == K:
    print(0)
else:
    print(bfs(N))
