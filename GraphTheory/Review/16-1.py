#https://www.acmicpc.net/problem/2637
#백준 2637번 장난감조립(위상정렬)
import sys
#input = sys.stdin.readline
sys.setrecursionlimit(100000)

def find_basic(target, cnt):
    if len(factory[target]) == 0:
        basic[target]+= 1*cnt
    else:
        for i in factory[target]:
            find_basic(i[0],i[1]*cnt)

n = int(input())
m = int(input())

factory = dict()
basic = dict()

for i in range(n):
    factory[i] = []

for _ in range(m):
    a, b, c = map(int, input().split())
    factory[a-1].append([b-1,c])
    
for i in range(n):
    if len(factory[i]) == 0:
        basic[i] = 0
        
find_basic(n-1, 1)

for i in basic:
    if basic[i] != 0:
        print(i+1, basic[i])
        
'''
재귀로 처리했더니 시간초과가 발생했다. 후 방식을 바꿔야 겠다...
deque로 처리하니까 메모리 초과가 발생했다... 해결법이 감이 안잡힌다.
정올에서는 문제없이 정답처리됨
'''