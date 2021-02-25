#https://www.acmicpc.net/problem/14496 최단 경로
#백준 14496번 그대, 그머가 되어
#백준 풀이 중에 dictionary를 활용한 다익스트라 풀이
import sys
import heapq
input=sys.stdin.readline
INF=sys.maxsize

def dijkstra(start):
    hq=[]
    res=[INF]*(n+1)
    res[start]=0
    heapq.heappush(hq,[0,start])
    while hq:
        dist,node=heapq.heappop(hq)
        for i in dic[node]:
            next=res[node]+1
            if next<res[i]:
                res[i]=next
                heapq.heappush(hq,[res[i],i])
    return res

a,b=map(int,input().split())
n,m=map(int,input().split())
dic={}
for i in range(1,n+1):
    dic.setdefault(i,[]) 
    '''
    key가 dictionary에 존재하지 않는 경우, key와 value를 추가하는 메서드.
    dictionary 내부에 key값이 존재하는 경우, 기존 그대로 유지되며 키,값이 추가되거나 변경되지 않는다.
    https://dongdongfather.tistory.com/68 이런 식으로 활용도 가능하다.
    '''
for _ in range(m):
    x,y=map(int,input().split())
    dic[x].append(y)
    dic[y].append(x) #값이 정해져 있지 않을 때에는 서로 입력을 해줘야 함
dist=dijkstra(a)
print(dist[b] if dist[b] != INF else -1)