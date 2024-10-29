# Q.
# 문자열 S가 주어졌을 때, 이 문자열에서 단어만 뒤집으려고 한다.
#
# 먼저, 문자열 S는 아래와과 같은 규칙을 지킨다.
#
# 알파벳 소문자('a'-'z'), 숫자('0'-'9'), 공백(' '),
# 특수 문자('<', '>')로만 이루어져 있다.
# 문자열의 시작과 끝은 공백이 아니다.
# '<'와 '>'가 문자열에 있는 경우 번갈아가면서 등장하며, '<'이 먼저 등장한다.
# 또, 두 문자의 개수는 같다.
#
# 태그는 '<'로 시작해서 '>'로 끝나는 길이가 3 이상인 부분 문자열이고,
# '<'와 '>' 사이에는 알파벳 소문자와 공백만 있다.
#
# 단어는 알파벳 소문자와 숫자로 이루어진 부분 문자열이고,
# 연속하는 두 단어는 공백 하나로 구분한다.
#
# 태그는 단어가 아니며, 태그와 단어 사이에는 공백이 없다.
#
# Input.
# 첫째 줄에 문자열 S가 주어진다. S의 길이는 100,000 이하이다.
#
# Ouput.
# 첫째 줄에 문자열 S의 단어를 뒤집어서 출력한다.


import sys
S = sys.stdin.readline().strip() + ' '
stack = []
result = ''
flag = 0

for i in S :
    if i == '<' :
        flag = 1
        for _ in range(len(stack)) :
            result += stack.pop()
    stack.append(i) # '<' 얘만 검사하고 append 하고 나머지는 순서상 검사없이 바로 append가 됨
    if i == '>' :
        flag = 0
        for _ in range(len(stack)) :
            result += stack.pop(0)
            # 그래서 여기에 '>'를 따로 append 하지 않아도 됨
    if i == ' ' and flag == 0 :
        stack.pop() # 마찬가지로 append가 된 채로 if문에 전달 되기 때문에 바로 pop()
        for _ in range(len(stack)) :
            result += stack.pop()
        result += ' ' # 띄어쓰기를 빼고 거꾸로 출력했으므로 띄어쓰기도 다시 출력해줌 (스택에 넣지는 않음)
print(result)




# 1. 단어가 어딘지 파악해야함
# 2. 어디까지가 한 단어인지 파악해야함
# 3. 단어 인덱스만 뒤집기
# 4. 태그인 경우만 제외하면 될듯?
# 5. 태그가 만들어지려면 무조건 <> 순서로 나와야함 <<는 될 수 없음
# 6. < 이게 나오면 그때부터 > 이게 나올때까지 길이 체크 (>=3)
# 7. 태그 길이 카운트가 시작되지 않았을때만 스택에 넣기
# 8. 스택을 두 개 사용해야 하는가? -> 출력때문에

# S = input()
# tag_stack = []
# string_stack = []
# pointer = 0
#
# for i in range(len(S)) :
#     tag_cnt = 0
#     if S[i] == '<' :
#         tag_cnt += 1
#         tag_stack.append(S[i])
#         while(S[i + tag_cnt] != '>') :
#             tag_stack.append(S[i + tag_cnt])
#             tag_cnt += 1
#         tag_stack.append(S[i + tag_cnt])
#         tag_cnt += 1
#         if tag_cnt >= 3 :
#             for j in range(tag_cnt) :
#                 print(tag_stack[j])
#         pointer = i + tag_cnt
#         i = pointer
#     if S[i] == '>' and S[i+1] != '<' :
#         k = i+1
#         while(S[k] != '<') :
#             string_stack.append(S[k])
#             if S[k] == ' ' :
#                 n = 0
#                 while(len(string_stack)-2) :
#                     print(string_stack[n])
#                     n += 1
#             k += 1
#
#         n = 0
#         while(len(string_stack)-2) :
#             print(string_stack[n])
#             n += 1
#
#         pointer = k
#         i = pointer


