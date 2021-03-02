#https://www.acmicpc.net/problem/1854 최단경로
#백준 1854번 K번째 최단경로 찾기(다익스트라)
#import sys
import heapq
#input = sys.stdin.readline

INF = int(1e9)
n, m, k = map(int, input().split())

info = [[] for _ in range(n)]
distance = [[INF]* k for _ in range(n)]

for _ in range(m):
    a, b, c = map(int, input().split())
    info[a - 1].append((c, b - 1))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    while q:
        dist, now = heapq.heappop(q)
        for i, j in info[now]: 
        #info는 (거리, 노드)로 구성되어 있기 때문에 변수 2개에 저장해줘야 오류 발생 X
            cost = dist + i
            if distance[j][k - 1] > cost:
                distance[j][k - 1] = cost
                distance[j].sort() 
                #정렬을 해야 distance 배열에 k에 맞추어 결과를 출력할 수 잇음
                heapq.heappush(q, (cost, j))

distance[0][0] = 0
dijkstra(0)  

for i in distance:
    if i[k - 1] == INF:
        print(-1)
    else:
        print(i[k - 1])
'''
초반에 어떤 방식으로 해결해야할 지 감이 잘 안잡혀서 오래 걸렸음.
기존의 다익스트라 문제와 다르게 k번째 위치를 어떻게 해결해야할지 몰라서 헤매다가
구글링을 통해 거리 배열을 n*k개로 만들고 정렬을 하면 길이를 기준으로 정렬 후
다익스트라를 적용하면 해결된다는 사실을 알았음. 
최단 경로 문제는 문제를 보고 무슨 알고리즘을 선택하기가 빡센거같음. 후...
'''