import sys
input = sys.stdin.readline
N = int(input())
stack = []
command = []
for i in range(N) :
    command.append(input().split())
    if len(command[i]) == 2 :
        stack.append(command[i][1])
    elif command[i][0] == 'pop' :
        if len(stack) == 0:
            print(-1)
        else:
            num = stack.pop()
            print(num)
    elif command[i][0] == 'size' :
        print(len(stack))
    elif command[i][0] == 'empty' :
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif command[i][0] == 'top' :
        if len(stack) == 0:
            print(-1)
        else:
            num = stack.pop()
            print(num)
            stack.append(num)


# def push(num) :
#     stack.append(num)
#
# def pop(stack) :
#     if len(stack) == 0 :
#         print(-1)
#     else :
#         num = stack.pop()
#         print(num)
#
# def size(stack) :
#     print(len(stack))
#
# def empty(stack) :
#     if len(stack) == 0 :
#         print(1)
#     else :
#         print(0)
#
# def top(stack) :
#     if len(stack) == 0 :
#         print(-1)
#     else :
#         num = stack.pop()
#         print(num)
#         stack.append(num)

