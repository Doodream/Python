N = int(input())
i = 1
count = 0
cnt = 0

# i가 주어진 수보다 크면 탈출
while True:
    i += cnt
    cnt += 6
    count += 1
    if i >= N:
        print(count)
        break
