#https://www.acmicpc.net/problem/2599
#백준 2599번 짝 정하기(그래프 이론, dfs)
#import sys
#input = sys.stdin.readline
n = int(input())
arr = []
for i in range(3):
    arr.append(list(map(int, input().split())))
some = 0
for i in arr:
    some += sum(i)
flag = 1
for x in range(arr[0][0]):
    ax = arr[0][0]- x
    y = n - arr[2][0] - arr[2][1] - x
    by = arr[1][0] - y
    z = arr[0][1] - y
    cz = arr[2][0] - z

    if (n == some/2) and (x >= 0) and (y >= 0) and (z >= 0) and(ax >= 0) & (by >= 0) and (cz >= 0):
        print(1)
        print(x, ax)
        print(y, by)
        print(z, cz)
        flag = 0
        break
if flag == 1:
    print(0)
'''
dfs로 해결할 수 있는 문제지만 문제를 보고 dfs가 바로 안 떠올랐다.
brute force밖에 안 떠올라서 검색하면서 문제를 풀었다. 
후... bfs랑 dfs는 문제를 보고 이렇게 풀어야 겠다 바로 안 떠오르는게 경험 부족같다...
'''