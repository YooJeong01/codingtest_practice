def self_num(n) :
    a = list(str(n))
    result = 0
    for i in range(len(a)) :
        result += int(a[i])
    result += n
    return result
results = set() # set으로 생성자 중복 제거
for i in range(10000) :
    results.add(self_num(i)) # 10000까지 모든 생성자를 넣는데 set 자료형이라 중복은 제거됨

for i in range(1,10001) : # result에 없는걸 출력하면 그게 self_number이 된다
    if i not in results :
        print(i)
