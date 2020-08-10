# 0 또는 양의 정수가 주어졌을 때, 정수를 이어 붙여 만들 수 있는 가장 큰 수를 알아내 주세요.
#
# 예를 들어, 주어진 정수가 [6, 10, 2]라면 [6102, 6210, 1062, 1026, 2610, 2106]를 만들 수 있고, 이중 가장 큰 수는 6210입니다.
#
# 0 또는 양의 정수가 담긴 배열 numbers가 매개변수로 주어질 때, 순서를 재배치하여 만들 수 있는 가장 큰 수를 문자열로 바꾸어 return 하도록 solution 함수를 작성해주세요.
#
# 제한 사항
# numbers의 길이는 1 이상 100,000 이하입니다.
# numbers의 원소는 0 이상 1,000 이하입니다.
# 정답이 너무 클 수 있으니 문자열로 바꾸어 return 합니다.
# 입출력 예
# numbers	return
# [6, 10, 2]	6210
# [3, 30, 34, 5, 9]	9534330

def solution(numbers):
    answer = []
    max = 0
    # map(str, numbers) 는 타입이 object이므로 자료형을 형변환 시켜줘야 한다.
    numbers = list(map(str, numbers))
    # 자동 들여쓰기 ctrl + alt + i
    # numbers에 max를 찾아서 하나씩 빼서 answer에 넣는다.
    # numbers이 없어 질때 까지 계속한다.
    while len(numbers) != 0:
        for i in range(0, len(numbers)):
            if i == 0:
                max = numbers[i]
            else:
                for j in range(0, len(numbers[i])):
                    # numbers[i]가 max보다 큰 자리 수 인 경우
                    if len(numbers[i]) > len(max):
                        # numbers[i] 이 300이고 max가 330 인경우 max가 더 앞에 있어야 하므로 break
                        if int(numbers[i]) % (10**(j+1)) == 0:
                            break
                        else:
                            max = numbers[i]
                            break
                    # 같은 자리수 인 경우 둘째 자리수 가 더 크다면
                    elif numbers[i][j] > max[j]:
                        max = numbers[i]
                    # 아얘 같은 수라면
                    elif numbers[i][j] == max[j]:
                        pass
                    else:
                        break

        numbers.remove(max)
        answer.append(max)
    # 문자열 바꾸기
    answer = ''.join(answer)
    answer = int(answer)
    answer = str(answer)

    return answer

numbers1 = [3, 30, 34, 5, 9, 4, 40, 42]
numbers2 = [3, 30, 34, 5, 9]
print(solution(numbers1))
