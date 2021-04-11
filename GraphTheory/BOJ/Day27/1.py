#https://www.acmicpc.net/problem/11725
#백준 11725번 트리의 부모 찾기(그래프 이론, dfs, bfs)
#import sys
#input = sys.stdin.readline
from collections import deque

n = int(input())
node = [0 for _ in range(n+1)]

tree = [[] for _ in range(n+1)]
for i in range(n-1):
    x, y = map(int, input().split())
    tree[x].append(y)
    tree[y].append(x)

q = deque()
q.append(1)
node[1] = 1
while q:
    cur = q.pop()

    for i in tree[cur]:
        if node[i] == 0: #방문하지 않은 경우
            node[i] = cur
            q.append(i)

for i in range(2, n+1):
    print(node[i])

'''
root 찾기로 풀 수 없는 문제였다. bfs로 풀면 될거 같은데 부모 node만 어떻게 지정할지
계속 고민하다가 구글링 해서 검색해보니까 애초에 한 번만 체크하도록 하면 바로 부모
node를 찾을 수 있었다. 문제 자체는 어렵지 않았는데 관점을 못잡아서 해매고 해설을 
찾아봤다... 후, 쉬운 문제를 틀리면 너무 허망해진다...
'''