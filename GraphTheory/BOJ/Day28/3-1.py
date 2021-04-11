#https://www.acmicpc.net/problem/2623
#백준 2623번 음악 프로그램(그래프 이론, 위상정렬)
#import sys
#input = sys.stdin.readline
from collections import deque

v,e = map(int,input().split()) 
graph=[[] for _ in range(v + 1)]
indegree=[0] * (v + 1)

for i in range(e): 
    data=list(map(int,input().split()))
    staff=data[0] 
    for j in range(1, staff):
        graph[data[j]].append(data[j+1])
        indegree[data[j+1]]+=1

q=deque()
for i in range(1, v+1):
    if indegree[i]==0:
        q.append(i)

cycle=False #cycle 여부를 check하는 변수
result=[]
for i in range(v):
    if len(q)==0: #큐가 비어있을 때, cycle이 발생
        cycle=True
        break
    cur=q.popleft()
    result.append(cur)
    for i in graph[cur]:
        indegree[i]-=1
        if indegree[i]==0:
            q.append(i)
if cycle:
    print(0)
else:
    for x in result:
        print(x)
'''
처음 보고 위상 정렬로 순서는 구현할 수 있겠는데 조건을 만족하지 않을 때 0를 어떻게
출력해야 할지 감을 못잡아서 결국 구글링을 해서 이해했다. 단순하게 생각해서
deque가 비어있다면 cycle이 발생한다는 뜻이기 때문에 이를 check하면 만족할 수 있다.
'''