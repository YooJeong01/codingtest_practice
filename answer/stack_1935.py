# Q.
# 후위 표기식과 각 피연산자에 대응하는 값들이 주어져 있을 때, 그 식을 계산하는 프로그램을 작성하시오.
#
# Input.
# 첫째 줄에 피연산자의 개수(1 ≤ N ≤ 26) 가 주어진다.
# 그리고 둘째 줄에는 후위 표기식이 주어진다.
# (여기서 피연산자는 A~Z의 영대문자이며, A부터 순서대로 N개의 영대문자만이 사용되며,
# 길이는 100을 넘지 않는다) 그리고 셋째 줄부터 N+2번째 줄까지는 각 피연산자에 대응하는 값이 주어진다.
# 3번째 줄에는 A에 해당하는 값, 4번째 줄에는 B에 해당하는값 , 5번째 줄에는 C ...이 주어진다,
# 그리고 피연산자에 대응 하는 값은 100보다 작거나 같은 자연수이다.
#
# 후위 표기식을 앞에서부터 계산했을 때, 식의 결과와 중간 결과가 -20억보다 크거나 같고,
# 20억보다 작거나 같은 입력만 주어진다.
#
# Output.
# 계산 결과를 소숫점 둘째 자리까지 출력한다.

# 1. 연산자가 나오기 전까지 stack.append()
# 2. 연산자가 나오면 pop()을 두번해서 연산자와 두 수를 계산 : n-1 @ n 이 순서로!
# 3. 계산한 값을 다시 stack.append()
# 4. 숫자가 나오면 append()
# 5. 연산자가 나오면 위 반복

n = int(input())
word = input()                # 후위표기식을 word에 저장함
num_lst = [0]*n				  # 피연산자값을 저장하기 위한 num_lst 생성

for i in range(n):
    num_lst[i] = int(input())  # 피연산자값 받기

stack = []                    # stack 리스트를 통해 후위표기식 계산

for i in word :
    if 'A' <= i <= 'Z' :		# 후위표기식에서 알파벳을 만나면 stack에 저장한다.(물론 알파벳 형태가 아닌 피연산자값의 형태로)
        stack.append(num_lst[ord(i)-ord('A')])
    else :						# 연산자를 만나면
        str2 = stack.pop()		# stack 리스트의 마지막 2항목을 꺼내와서 계산한다.
        str1 = stack.pop()

        if i =='+' :
            stack.append(str1+str2)
        elif i == '-' :
            stack.append(str1-str2)
        elif i == '*' :
            stack.append(str1*str2)
        elif i == '/' :
            stack.append(str1/str2)

print('%.2f' %stack[0])

# N = int(input())
# word = input()
# value = []
#
# for i in range(N) :
#     value[i]=int(input())
#
# stack = []
# for i in range(word) :
#     if 'A' <= i <= 'Z':
#         stack.append(value[ord(i)-ord('A')])
#
#     else :
#         a = stack.pop()
#         b = stack.pop()
#         if i == '*' :
#             stack.append(a * b)
#         if i == '/' :
#             stack.append(a / b)
#         if i == '+' :
#             stack.append(a + b)
#         if i == '-' :
#             stack.append(a - b)
# print('%.2f' %stack[0])



