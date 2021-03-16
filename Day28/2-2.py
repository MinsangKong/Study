#https://www.acmicpc.net/problem/2252
#백준 2252번 줄 세우기(그래프이론, DFS)
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
g = [[] for i in range(N)]
cycle = 0
v = [0] * N
f = [0] * N
order = []

def DFS(cur):
    global cycle
    if cycle:
        return
    v[cur] = 1
    for nxt in g[cur]:
        if not v[nxt]: #방문 여부
            DFS(nxt)
        elif not f[nxt]:
            cycle = 1
        
    f[cur] = 1
    order.append(cur+1)

for i in range(M):
    a, b = map(int, input().split())
    g[a-1].append(b-1)

for cur in range(N):
    if not v[cur]:
        DFS(cur)

if cycle:
    print(0)
else:
    print(*order[::-1])
'''
DFS를 적용해서 풀 수도 있는 문제였다. DFS로 풀 경우에는 선수과목에 대해 flag 변수를
추가로 만들어서 DFS를 처리를 하는 중에 선수과목에 대한 처리가 필요했다. 또한 
위상 정렬 때와 반대로 진출하는 노드들을 리스트로 저장하고 있는 것이 아니라 
진입해오는 노드들에 대해서 리스트로 저장하거나 DFS 한뒤 역으로 출력해야
문제를 해결할 수 있다.
DFS 설명 : https://suri78.tistory.com/202
'''