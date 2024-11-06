n = int(input())

arr = list(map(int, input().split()))
answer = [0] * n

for i in range(n):
    cnt = 0
    for j in range(n):
        if cnt == arr[i] and answer[j] == 0: # 빈자리를 만들어 둔 후(cnt) 내 자리에 아무것도 없을 경우 값 넣기
            answer[j] = i + 1
            break
        elif answer[j] == 0:
            cnt += 1

print(' '.join(map(str, answer)))