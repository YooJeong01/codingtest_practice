

N = int(input())
R = int(input())
candidates = list(map(int, input().split()))
post = {}
# 딕셔너리는 리스트와 다르게 0부터 생성되는게 아니라, 뜬금없이 2가 생성이 될 수도 있는 자료구조임

for i in range(R) :
    if post.get(candidates[i]) :
        post[candidates[i]] += 1
        # post의 값으로는 추천수가 들어가고, post의 인덱스가 후보자가 된다
        # ex. post[2] = 5 라면 후보자 2가 추천수 5개를 받은것
    else :
        if len(post) == N : # 딕셔너리를 썼기 떄문에 위와같은 작업을 하고도 연산했을때 조건문이 가능함
            min_value = R
            for key in reversed(post.keys()) :
                if min_value >= post[key] :
                    min_value = post[key]
                    min_key = key
            post.pop(min_key)
            post[candidates[i]] = 1
        else :
            post[candidates[i]] = 1
sorted_keys = sorted(post.keys(), key = int)

for key in sorted_keys :
    print(key, end=' ')
print()

# for i in vote :
#     candidates[i].append((i,candidates[i][1]+1))
#     if len(post) == N :
#         post.sort(key=lambda x:[1], reverse=True)
#         a, like_cnt = post.pop()
#         candidates[a][1] = 0
#     post.append(candidates[i])
#
# post.sort(key=lambda x:[0])
# print(post)

