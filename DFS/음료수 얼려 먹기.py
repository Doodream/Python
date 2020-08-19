# N * M 크기의 얼음 틀이 있다. 구멍이 뚫려 있는 부분은 0, 칸막이가 존재하는 부분은 1로
# 표시된다. 구멍이 뚫려 있는 부분끼리 상, 하, 좌, 우로 붙어있는 경우 서로 연결되어있는 것으로 간주한다.
# 이때 얼음 틀의 모양이 주어졌을 떄 생성되는 총 아이스크림의 개수를 구하는 프로그램을 작성하시오.
# 다음의 4 * 5 얼음틀 예시에서는 아이스크림이 총 3개 생성된다.
#
#  00110
#  00011
#  11111
#  00000

# 입력조건
# - 첫 번째 줄에 얼음 틀의 세로길이 N과 가로 길이 M이 주어진다.(1 <= N, M <= 1000)
# - 두 번째 줄부터 N + 1번째 줄 까지 얼음 틀의 형태가 주어진다.
# - 이때 구멍이 뚫려 있는 부분은 0, 그렇지 않은 부분은 1이다.
#
# 출력조건
# - 한 번에 만들수 있는 아이스크림의 개수를 출력한다.

N, M = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, input())))
answer = 0

def dfs(x, y):
    if x < 0 or x > N - 1 or y < 0 or y > M - 1:
        return False
    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y + 1)
        dfs(x, y - 1)
        return True


    return False

for i in range(N):
    for j in range(M):
        if dfs(i, j) == True:
            answer += 1

print(answer)






