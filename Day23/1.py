#https://www.acmicpc.net/problem/2224
#백준 2224번 명제 증명(플로이드)
#어케 풀어야할지 감을 못 잡아서 구글링 후 이해
import sys

input = sys.stdin.readline
INF = int(1e9)  # 무한을 의미하는 값으로 10억을 설정

# 2차원 리스트(그래프 표현)를 만들고, 모든 값을 무한으로 초기화
graph = [[INF] * (52) for _ in range(52)]

for _ in range(int(input())):
    a, b, c = input().split()

    a_ord = ord(a)
    c_ord = ord(c)

    # 소문자
    if a_ord >= ord('a'):
        a_ord = a_ord - (ord('a') - ord('Z') - 1)
    # 소문자
    if c_ord >= ord('a'):
        c_ord = c_ord - (ord('a') - ord('Z') - 1)

    a_ord = a_ord - ord('A')
    c_ord = c_ord - ord('A')

    graph[a_ord][c_ord] = 1

# 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
for a in range(52):
    for b in range(52):
        if a == b:
            graph[a][b] = 0

# 점화식에 따라 플로이드 워셜 알고리즘을 수행
for k in range(52):
    for a in range(52):
        for b in range(52):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

arr = []
# 수행된 결과를 출력
for a in range(52):
    for b in range(52):
        # 도달할 수 없는 경우, 무한(INFINITY)이라고 출력
        if graph[a][b] == 0 or graph[a][b] == 1e9:
            pass
        # 도달할 수 있는 경우 거리를 출력
        else:
            arr.append(a)
            arr.append(b)
            # print(graph[a][b], end=" ")

print(len(arr) // 2)
for i in range(0, len(arr), 2):
    # print(arr[i], arr[i+1])
    a = arr[i]
    c = arr[i + 1]
    
    # 소문자
    if a > 25:
        a = a + (ord('a') - ord('Z') - 1)
    # 소문자
    if c > 25:
        c = c + (ord('a') - ord('Z') - 1)

    a = a + ord('A')
    c = c + ord('A')

    print("%c => %c" % (chr(a), chr(c)))