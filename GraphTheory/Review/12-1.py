#https://www.acmicpc.net/problem/21276
#백준 21276번 계보 복원가 호석(위상정렬)
#import sys
#input = sys.stdin.readline
from collections import deque

n = int(input())
names = list(input().split())

family = dict()
indegree = dict()
result = dict()

for name in names:
    family[name] = []
    indegree[name] = 0
    result[name] = []

m = int(input())

for _ in range(m):
    c, p = input().split()
    family[p].append(c)
    indegree[c]+=1
    
origin = []
for i in indegree:
    if indegree[i] == 0:
        origin.append(i)
        
print(len(origin))
origin.sort()
print(*origin)

origin = deque(origin)
while origin:
    now = origin.popleft()
    
    for i in family[now]:
        indegree[i] -= 1
        if indegree[i] == 0:
            origin.append(i)
            result[now].append(i)
            
for i in sorted(result):
    print(i, len(result[i]), *sorted(result[i]))
    