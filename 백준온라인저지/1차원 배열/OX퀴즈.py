# 문제
# "OOXXOXXOOO"와 같은 OX퀴즈의 결과가 있다. O는 문제를 맞은 것이고, X는 문제를 틀린 것이다.
# 문제를 맞은 경우 그 문제의 점수는 그 문제까지 연속된 O의 개수가 된다. 예를 들어, 10번 문제의 점수는 3이 된다.
#
# "OOXXOXXOOO"의 점수는 1+2+0+0+1+0+0+1+2+3 = 10점이다.
#
# OX퀴즈의 결과가 주어졌을 때, 점수를 구하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 테스트 케이스의 개수가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있고,
# 길이가 0보다 크고 80보다 작은 문자열이 주어진다. 문자열은 O와 X만으로 이루어져 있다.
#
# 출력
# 각 테스트 케이스마다 점수를 출력한다.
#
# 예제 입력 1
# 5
# OOXXOXXOOO
# OOXXOOXXOO
# OXOXOXOXOXOXOX
# OOOOOOOOOO
# OOOOXOOOOXOOOOX
# 예제 출력 1
# 10
# 9
# 7
# 55
# 30


import sys
N = int(sys.stdin.readline())
# 80줄 안쪽의 행바꿈을 이용해 입력을 받으므로
# 문자열을 이용하여 해결을 하므로 입력에 대한 형변환 하지 않음

# Quiz_result = [sys.stdin.readline() for i in range(80)] 이러한 형태는 정확하게 길이가 확인될 경우가능 아니라면 try except

score_total = 0
score = 0
Quiz_result = []

# Quiz결과의 여러줄을 이중 반복문으로 해결

# while True:
#     text = sys.stdin.readline()
#     # text의 공백을 제거함으로서 끝나는 문자의 끝을 빈공간과 같게해서 문자입력을 끝냄
#     if text.strip() == stoptext:
#         break
#     Quiz_result.append(text)

Quiz_result = [sys.stdin.readline() for i in range(N)]

for i in range(len(Quiz_result)):
    for j in range(len(Quiz_result[i])):
        if Quiz_result[i][j] == 'O':
            score += 1
            score_total += score
        else:
            score = 0
    print(score_total)
    score_total = 0



