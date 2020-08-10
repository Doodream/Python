text = input()
# 대문자와 소문자를 통일시켜야 한다.
# upper	주어진 문자열에서 모든 알파벳들을 대문자로 변환시킨다.
# capitalize	주어진 문자열에서 맨 첫 글자를 대문자로 변환시킨다.
# title	주어진 문자열에서 알파벳 외의 문자(숫자, 특수기호, 띄어쓰기 등)로 나누어져 있는 영단어들의 첫 글자를 모두 대문자로 변환시킨다.
text = list(text.upper())
text_temp = text
repeat_alphabet = []

# 클론 텍스트에서 알파벳 하나하나 갯수를 세고
for i in text_temp:
    if text_temp.index(i) == 0:
        max_count = text_temp.count(i)
        # 첫번쨰로 나왔다고 text에서 지워도 괜찮음/ 만약 첫번째가 많이 나왔다면 하나지워도 set(text)에는 원소가 남게됨.
        text.remove(i)
    # repeat_alphabet.append(text_temp.count(i))
    # 만약 가장 많이 나온 알파벳 횟수보다 같거나 많이 나왔다면 max_count 스왑
    elif text_temp.count(i) >= max_count:
        max_count = text_temp.count(i)
    # max.count 보다 적은 횟수로 알파벳이 나왔다면 text 문자열에서 지워버린다.
    else:
        text.remove(i)
# 중복된 원소는 지워버리고
text = set(text)

# 만약 text에서 원소 갯수가 2개 이상이라면 ? 출력
if len(text) > 1:
    print('?')

# 아니라면 해당원소 출력
else:
    print(list(text)[0])

# pop함수는 리스트의 원소가 어디위치 인지 반납하고 해당 위치의 원소를 꺼낸다. a.pop(위치) 인수가 없을 경우 마지막 원소를 꺼낸다.
# index함수는 리스트의 원소가 어디위치인지 반납한다.