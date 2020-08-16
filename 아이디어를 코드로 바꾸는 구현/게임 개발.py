# 현민이는 게임캐릭터가 맵 안에서 움직이는 시스템을 개발중이다.
# 캐릭터가 있는 장소는 1 * 1 크기의 정사각형으로 이뤄진 N * M 크기의 직사각형으로, 각각의 칸은 육지 또는 바다이다.
# 캐릭터는 동서남북 중 한 곳을 바라본다.
#
# 맵의 각칸은 (A, B)로 나타낼 수 있고, A는 북쪽으로부터 떨어진 칸의 갯수, B는 서쪽으로부터
# 떨어진 칸의 개수이다. 캐릭터는 상하좌우로 움직일 수 있고, 바다로 되어 있는 공간에는 갈 수 없다.
# 캐릭터의 움직임을 설정하기 위해 정해놓은 매뉴얼은 이러하다.
#
# 1. 현재 위치에서 현재 방향을 기준으로 왼쪽 방향(반시계 방향으로 90도 회전한 방향)부터 차례대로 갈 곳을 정한다.
#
# 2. 캐릭터의 바로 왼쪽 방향에 아직 가보지 않은 칸이 존재한다면,
# 왼쪽 방향으로 회전한 다음 왼쪽으로 한 칸을 전진 한다.
# 왼쪽 방향에 가보지 않은 칸이 없다면, 왼쪽 방향으로 회전만 수행하고 1단계로 돌아간다.
#
# 3. 만약 네 방향 모두 이미 가본 칸이거나 바다로 되어있는 칸인 경우에는,
# 바라보는 방향을 유지한 채로 한 칸 뒤로 가고 1단계로 돌아간다.
# 단, 이때 뒤쪽 방향이 바다인 칸이라 뒤로 갈 수 없는 경우에는 움직임을 멈춘다.
#
# 현민이는 위과정을 반복적으로 수행하면서 캐릭터의 움직임에 이상이 있는지 테스트 하려고 한다.
# 매뉴얼에 따라 캐릭터를 이동시킨 뒤에, 캐릭터가 방문한 칸의 수를 출력하는 프로그램을 만드시오.
#
# 입력조건
# - 첫째 줄에 맵의 세로 크기 N과 가로 크기 M을 공백으로 구분하여 입력한다. (N >= 3. M <= 50)
# - 둘째 줄에 게임 캐릭터가 있는 칸의 좌표(A, B)와 바라보는 방향 d가 각각 서로 공백으로 구분하여 주어진다.
# 방향 d의 값은 다음과 같다.
# - 0: 북쪽
# - 1: 동쪽
# - 2: 남쪽
# - 3: 서쪽
#
# 셋째 줄부터는 맵이 육지인지 바다인지 입력한다. N개의 줄에 맵의 상태가 북쪽부터 남쪽 순서대로,
# 각 줄의 데이터는 서쪽부터 동쪽 순서대로 주어진다. 맵의 외곽은 항상 바다로 되어있다.
# - 0: 육지
# - 1: 바다
#
# - 처음에 게임 캐릭터가 위치한 칸의 상태는 항상 육지이다.
#
# 출력조건
# - 첫째 줄에 이동을 마친 후 캐릭터가 방문한 칸의 수를 출력한다.
#
#
# 입력예시
# 4 4
# 1 1 0
# 1 1 1 1
# 1 0 0 1
# 1 1 0 1
# 1 1 1 1
#
# 출력예시
# 3

import copy
# 방향전환
def change_direction(tmp):
    if tmp[2] == 0:
        tmp[2] = 3
    elif tmp[2] == 1:
        tmp[2] = 0
    elif tmp[2] == 2:
        tmp[2] = 1
    else:
        tmp[2] = 2
    return tmp

# 해당방향으로 직진
def go_step(tmp):
    if tmp[2] == 0:
        tmp[0] -= 1
    elif tmp[2] == 1:
        tmp[1] += 1
    elif tmp[2] == 2:
        tmp[0] += 1
    else:
        tmp[1] -= 1
    return tmp

# 후진
def reverse_step(tmp):
    if tmp[2] == 0:
        tmp[0] += 1
    elif tmp[2] == 1:
        tmp[1] -= 1
    elif tmp[2] == 2:
        tmp[0] -= 1
    else:
        tmp[1] += 1
    return tmp

N, M = map(int, input().split())
location = list(map(int, input().split()))

game_map = []
for i in range(N):
    game_map.append(list(map(int, input().split())))

# 캐릭터는 입장하자마자 한개의 칸을 방문한다.
step = 1
direction_count = 0

while True:
        pre_location = copy.deepcopy(location)
        pre_location = change_direction(pre_location)
        pre_location = go_step(pre_location)

        # 한번도 가보지 안은 방향이든 가본 방향이든 방향은 변함
        # 방향 전환
        location = change_direction(location)

        # 캐릭터의 왼쪽방향이 한번도 가보지 않은 방향
        if game_map[pre_location[0]][pre_location[1]] == 0:
            # 한칸 이동
            location = go_step(location)
            step += 1
            # 이미 가본칸은 1로 표시 : 가본칸이나 바다인 경우나 못가는 건 똑같기 때문에
            game_map[location[0]][location[1]] = 1
            direction_count = 0
        # 캐릭터의 왼쪽방향이 바다 이거나 가본 방향
        else:
            direction_count += 1
        # 캐릭터의 사방이 바다 이거나 가본 방향인 경우
        if direction_count == 4:

            pre_location = reverse_step(location)
            # 후진 했을 때 바다라면
            if game_map[pre_location[0]][pre_location[1]] == 1:
                # 움직임 끝
                break
            else:
                # 후진
                location = reverse_step(location)

print(step)
