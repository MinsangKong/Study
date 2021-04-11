#https://www.acmicpc.net/problem/2056
#백준 2056번 작업(그래프이론, 위상정렬)
#import sys
#input = sys.stdin.readline

n = int(input())
times = [0] * (n+1)
graph = {}
for i in range(1, n+1):
    data = list(map(int, input().split()))
    times[i] = data[0]
    if data[1] > 0:
        for j in data[2:]:
            if i in graph:
                graph[i].append(j)
            else:
                graph[i] = [j]
            
for i in range(1, n+1):
    if i in graph:
        time = 0
        for j in graph[i]:
            time = max(time, times[j])
        times[i] += time
        
print(max(times))
'''
서로 선행 관계가 없는 작업들은 동시에 수행 가능하다. 이 부분을 못봐서
계속 틀리고 엄청 해멨다...
'''