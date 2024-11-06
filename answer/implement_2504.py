# 1. 여는 괄호는 append
# 2. 닫는 괄호가 나오면 직전껄 pop 하고 종류에 따라서 *3 등


# Answer
# 1. 일단 입력받을떄 그냥 input()으로만 입력받으면 글자 수 안주고도 글자 길이만큼만 입력이 받아진다
# 2. 그리고 괄호를 직접 append 하는 아이디어 까진 좋았는데
# 3. 결과 계산이 이상했음
# 4. 답에서는 tmp라는 인자에 *2, *3을 누적하고
# 5. 닫는 짝 괄호가 나오면 그떄 + 를 해준다
# 6. 무결성 검사도 필수

lis = input()

stack = []
result = 0
tmp = 1
for i in range(len(lis)) :
    if lis[i] == "(" :
        stack.append(lis[i])
        tmp *= 2
    elif lis[i] == "[" :
        stack.append(lis[i])
        tmp *= 3
    elif lis[i] == ")" :
        if not stack or stack[-1] == "[" :
            result = 0
            break
        if lis[i-1] == "(" :
            result += tmp
        stack.pop()
        tmp //= 2
    else :
        if not stack or stack[-1] == "(" :
            result = 0
            break
        if lis[i-1] == "[" :
            result += tmp
        stack.pop()
        tmp //= 3


if stack :
    print(0)
else :
    print(result)

