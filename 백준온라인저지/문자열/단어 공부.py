# 단어 공부 분류
# 시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
# 2 초	128 MB	64858	24601	19936	38.556%
# 문제
# 알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오. 단, 대문자와 소문자를 구분하지 않는다.
#
# 입력
# 첫째 줄에 알파벳 대소문자로 이루어진 단어가 주어진다. 주어지는 단어의 길이는 1,000,000을 넘지 않는다.
#
# 출력
# 첫째 줄에 이 단어에서 가장 많이 사용된 알파벳을 대문자로 출력한다. 단, 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력한다.
#
# 예제 입력 1
# Mississipi
# 예제 출력 1
# ?
# 예제 입력 2
# zZa
# 예제 출력 2
# Z
# 예제 입력 3
# z
# 예제 출력 3
# Z
# 예제 입력 4
# baaa
# 예제 출력 4
# A

text = input().upper()
# 대문자와 소문자를 통일시켜야 한다.
# upper	주어진 문자열에서 모든 알파벳들을 대문자로 변환시킨다.
# capitalize	주어진 문자열에서 맨 첫 글자를 대문자로 변환시킨다.
# title	주어진 문자열에서 알파벳 외의 문자(숫자, 특수기호, 띄어쓰기 등)로 나누어져 있는 영단어들의 첫 글자를 모두 대문자로 변환시킨다.
# enumerate(turple, set, list, dictionary, string) -> index 와 원소를 가지는 객체를 반환
repeat_alphabet = []
for i in set(text):
    repeat_alphabet.append(text.count(i))

# idx = []
# for i, x in enumerate(repeat_alphabet):
#     if x == max(repeat_alphabet):
#         idx.append(i)
# 을 한줄로 요약
idx = [i for i, x in enumerate(repeat_alphabet) if x == max(repeat_alphabet)]
# 원소수가 가장많은 값을 가진것이 2개 이상일때
if len(idx) > 1:
    print('?')
# 아니라면 가장많은 원소는 하나이므로 해당원소 출력
else:
    # 중복을 걸러낸 text 리스트에 가장 많이 나온 값의 인덱스를 출력
    print(list(set(text))[repeat_alphabet.index(max(repeat_alphabet))])

# pop함수는 리스트의 원소가 어디위치 인지 반납하고 해당 위치의 원소를 꺼낸다. a.pop(위치) 인수가 없을 경우 마지막 원소를 꺼낸다.
# index함수는 리스트의 원소가 어디위치인지 반납한다.
