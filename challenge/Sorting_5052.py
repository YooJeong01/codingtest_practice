# 문제를 봤을때 한 자리 한 자리마다 트리 처럼 분류가 갈라져야 하나? 생각해서 해결법이 떠오르지 않았음
# -> 풀이를 보니, 한 번호라도 포함을 하냐 안하냐로 구분
# ex. 111 / 111222 에서 111222는 111을 포함하므로 일관성 X

# Anwer

T = int(input())
for _ in range(T) :
    phone = []
    result = "YES"
    N = int(input())
    for i in range(N) :
        phone.append(input())
    phone.sort()
    for i in range(N-1) :
        if phone[i] == phone[i+1][:len(phone[i])] :
            result = "NO"
    print(result)
