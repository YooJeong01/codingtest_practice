import sys
input = sys.stdin.readline
N = int(input())
command = []
deck = []
for i in range(N) :
    command.append(input().split())
    if command[i][0] == 'push_front' :
        deck.insert(0,command[i][1])
    elif command[i][0] == 'push_back' :
        deck.append(command[i][1])
    elif command[i][0] == 'pop_front' :
        if len(deck) == 0 : print(-1)
        else:
            num = deck.pop(0)
            print(num)
    elif command[i][0] == 'pop_back' :
        if len(deck) == 0: print(-1)
        else :
            num = deck.pop()
            print(num)
    elif command[i][0] == 'size' :
        print(len(deck))
    elif command[i][0] == 'empty' :
        if len(deck) == 0 : print(1)
        else : print(0)
    elif command[i][0] == 'front' :
        if len(deck) == 0 : print(-1)
        else :
            print(deck[0])
    elif command[i][0] == 'back' :
        if len(deck) == 0 : print(-1)
        else :
            print(deck[-1])
