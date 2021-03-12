#https://www.acmicpc.net/problem/9372
#백준 9372번 상근이의 여행(그래프 이론, bfs)
import sys
T=int(sys.stdin.readline())
 
for _ in range(T):
    N,M=map(int,sys.stdin.readline().split())
    for _ in range(M):
        a,b=map(int,sys.stdin.readline().split())
    print(N-1)
''' 
문제 조건에서 비행 스케줄은 항상 연결 그래프를 이루기 때문에
각 국가를 연결하는  최소연결 수인 N-1이 정답이된다... 허망하다...
https://gmlwjd9405.github.io/2018/08/28/algorithm-mst.html
'''