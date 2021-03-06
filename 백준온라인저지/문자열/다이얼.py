# 문제
# 상근이의 할머니는 아래 그림과 같이 오래된 다이얼 전화기를 사용한다.
#
#
#
# 전화를 걸고 싶은 번호가 있다면, 숫자를 하나를 누른 다음에 금속 핀이 있는 곳 까지 시계방향으로 돌려야 한다. 숫자를 하나 누르면 다이얼이 처음 위치로 돌아가고, 다음 숫자를 누르려면 다이얼을 처음 위치에서 다시 돌려야 한다.
#
# 숫자 1을 걸려면 총 2초가 필요하다. 1보다 큰 수를 거는데 걸리는 시간은 이보다 더 걸리며, 한 칸 옆에 있는 숫자를 걸기 위해선 1초씩 더 걸린다.
#
# 상근이의 할머니는 전화 번호를 각 숫자에 해당하는 문자로 외운다. 즉, 어떤 단어를 걸 때, 각 알파벳에 해당하는 숫자를 걸면 된다. 예를 들어, UNUCIC는 868242와 같다.
#
# 할머니가 외운 단어가 주어졌을 때, 이 전화를 걸기 위해서 필요한 시간을 구하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 알파벳 대문자로 이루어진 단어가 주어진다. 단어는 2글자~15글자로 이루어져 있다.
#
# 출력
# 첫째 줄에 다이얼을 걸기 위해서 필요한 시간을 출력한다.
#
# 예제 입력 1
# UNUCIC
# 예제 출력 1
# 36

text = input()
times = 0

for i in text:
    if i == 'A' or i == 'B' or i == 'C':
        times += 3
    elif i == 'D' or i == 'E' or i == 'F':
        times += 4
    elif i == 'G' or i == 'H' or i == 'I':
        times += 5
    elif i == 'J' or i == 'K' or i == 'L':
        times += 6
    elif i == 'N' or i == 'M' or i == 'O':
        times += 7
    elif i == 'P' or i == 'Q' or i == 'R' or i == 'S':
        times += 8
    elif i == 'T' or i == 'U' or i == 'V':
        times += 9
    else:
        times += 10

times = 0
print(times)

# # 다른해답
# dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
#
# for i in text:
#     for j, x  in enumerate(dial):
#         if i in x:
#             times += j + 3
#
# print(times)


