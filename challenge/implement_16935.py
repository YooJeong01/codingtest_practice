import sys
input = sys.stdin.readline
from copy import deepcopy

# 1번 상하반전
# 2번 좌우반전
# 3번 오른쪽 90도
# 4번 왼쪽 90도
# 5번 N/2 x M/2 4개 나눠서 오른쪽
# 6번 왼쪽

def rotate1():
    for i in range(N):
        arr[i] = new_arr[N-i-1]

def rotate2():
    for i in range(N):
        for j in range(M):
            arr[i][j] = new_arr[i][M-1-j]

def rotate3():
    global arr, N, M
    arr = list(map(list, zip(*arr[::-1])))
    N, M = M, N

def rotate4():
    global arr, N, M
    arr = list(map(list, zip(*arr)))[::-1]
    N, M = M, N

def rotate5():
    global arr
    for i in range(N//2):
        for j in range(M//2):
            arr[i][j] = new_arr[i+N//2][j]
            arr[i][j+M//2] = new_arr[i][j]
            arr[i+N//2][j+M//2] = new_arr[i][j+M//2]
            arr[i+N//2][j] = new_arr[i+N//2][j+M//2]

def rotate6():
    global arr
    for i in range(N//2):
        for j in range(M//2):
            arr[i][j] = new_arr[i][j+M//2]
            arr[i][j+M//2] = new_arr[i+N//2][j+M//2]
            arr[i+N//2][j+M//2] = new_arr[i+N//2][j]
            arr[i+N//2][j] = new_arr[i][j]

N, M, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
command = list(map(int, input().split()))


for c in command:
    new_arr = deepcopy(arr)
    if c == 1:
        rotate1()
    elif c == 2:
        rotate2()
    elif c == 3:
        rotate3()
    elif c == 4:
        rotate4()
    elif c == 5:
        rotate5()
    else:
        rotate6()
for a in arr:
    print(*a)


# def cal_TB(graph, n, m) :
#     tmp = [[0]*m for _ in range(n//2)]
#     for j in range(n//2) :
#         for k in range(m) :
#             tmp[j][k] = graph[j][k]
#             graph[j][k] = graph[n-j-1][k]
#             graph[n-j-1][k] = tmp[j][k]
#     return graph
#
# def cal_LR(graph, n, m) :
#     tmp = [[0]*(m//2) for _ in range(n)]
#     for j in range(n) :
#         for k in range(m//2) :
#             tmp[j][k] = graph[j][k]
#             graph[j][k] = graph[j][m-k-1]
#             graph[j][m-k-1] = tmp[j][k]
#     return graph
#
# def cal_R90(graph, n, m) :
#     tmp = [[0]*m for _ in range(n)]
#     for j in range(n) :
#         for k in range(m) :
#             tmp[k][n-j-1] = graph[j][k]
#     return tmp
#
# def cal_L90(graph, n, m) :
#     tmp = [[0]*m for _ in range(n)]
#     for j in range(n) :
#         for k in range(m) :
#             tmp[m-k-1][j] = graph[j][k]
#     return tmp
#
# def cal_quaterR90(graph, n, m) :
#     n = n//2
#     m = m//2
#     tmp = [[0]*m for _ in range(n)]
#
#     for j in range(n) :
#         for k in range(m) :
#             tmp[j][k] = graph[j][k]
#             graph[j][k] = graph[j+n][k]
#             graph[j+n][k] = graph[j+n][k+m]
#             graph[j+n][k+m] = graph[j][k+m]
#             graph[j][k+m] = tmp[j][k]
#     return graph
#
# def cal_quaterZ(graph, n, m) :
#     n = n//2
#     m = m//2
#     tmp = [[0]*m for _ in range(n)]
#
#     for j in range(n) :
#         for k in range(m) :
#             tmp[j][k] = graph[j][k]
#             graph[j][k] = graph[j][k+m]
#             graph[j][j+m] = graph[j+n][k+m]
#             graph[j+n][k+m] = graph[j+n][k]
#     return graph
#
#
# n, m, c = map(int, input().split())
# graph = []
# for _ in range(n) :
#     graph.append(list(map(int,input().split())))
# cal_num = int(input())
#
# if cal_num == 1 :
#     while c > 0 :
#         cal_TB(graph, n, m)
#         c -= 1
# elif cal_num == 2 :
#     while c > 0 :
#         cal_LR(graph, n, m)
#         c -= 1
# elif cal_num == 3 :
#     while c > 0 :
#         cal_R90(graph, n, m)
#         c -= 1
# elif cal_num == 4 :
#     while c > 0 :
#         cal_L90(graph, n, m)
#         c -= 1
# elif cal_num == 5 :
#     while c > 0 :
#         cal_quaterR90(graph, n, m)
#         c -= 1
# elif cal_num == 6 :
#     while c > 0 :
#         cal_quaterZ(graph, n, m)
#         c -= 1
#
# for i in range(n) :
#     print(graph[i])




