# 문제
# 예전에는 운영체제에서 크로아티아 알파벳을 입력할 수가 없었다. 따라서, 다음과 같이 크로아티아 알파벳을 변경해서 입력했다.
#
# 크로아티아 알파벳	변경
# č	c=
# ć	c-
# dž	dz=
# đ	d-
# lj	lj
# nj	nj
# š	s=
# ž	z=
# 예를 들어, ljes=njak은 크로아티아 알파벳 6개(lj, e, š, nj, a, k)로 이루어져 있다. 단어가 주어졌을 때, 몇 개의 크로아티아 알파벳으로 이루어져 있는지 출력한다.
#
# dž는 무조건 하나의 알파벳으로 쓰이고, d와 ž가 분리된 것으로 보지 않는다. lj와 nj도 마찬가지이다. 위 목록에 없는 알파벳은 한 글자씩 센다.
#
# 입력
# 첫째 줄에 최대 100글자의 단어가 주어진다. 알파벳 소문자와 '-', '='로만 이루어져 있다.
#
# 단어는 크로아티아 알파벳으로 이루어져 있다. 문제 설명의 표에 나와있는 알파벳은 변경된 형태로 입력된다.
#
# 출력
# 입력으로 주어진 단어가 몇 개의 크로아티아 알파벳으로 이루어져 있는지 출력한다.
#
# 예제 입력 1
# ljes=njak
# 예제 출력 1
# 6
# 예제 입력 2
# ddz=z=
# 예제 출력 2
# 3
# 예제 입력 3
# nljj
# 예제 출력 3
# 3
# 예제 입력 4
# c=c=
# 예제 출력 4
# 2

C_alphabet = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

text = input()
text_list = []
ret = 0

for j in C_alphabet:
    # text에서 j를 추출후 text 재건
    while j in text:
        # j를 text_list 포함, j를 제외한 문자열을 다시 만들것
        slice = text.index(j)
        front_slice = ' ' + text[:slice]
        back_slice = ' ' + text[slice + len(j):]
        text = front_slice + back_slice
        text_list.append(j)
        text = text.strip()

text_list = text_list + list(''.join(text))
# text_list안의 ' '제거
while ' ' in text_list:
    text_list.remove(' ')
print(len(text_list))

# 해답
# a = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
# alpha = input()
# for t in a:
#     alpha = alpha.replace(t, '*')
# print(len(alpha))
#
# 출처: https://hongku.tistory.com/255 [IT에 취.하.개.]