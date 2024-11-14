# T의 길이 - S의 길이 만큼의 횟수만에 만들 수 있어야 함!

# Answer
# 탑다운 방식으로 접근
# 하나씩 추가하는 방법은 다양한 경우의 수가 있으므로
# 최종본을 하나씩 지워가면서, 수행을 했을 때 같아졌는지 비교!
S = list(map(str,input()))
T = list(map(str,input()))

for _ in range(len(T)-len(S)) :
    if T[-1] == "A" :
        T.pop()
    elif T[-1] == "B" :
        T.pop()
        T.reverse()

if S == T :
    print(1)
else : print(0)