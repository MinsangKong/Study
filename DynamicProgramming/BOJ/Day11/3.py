#https://www.acmicpc.net/problem/1932
#백준 1932번 정수 삼각형
n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))
    
for i in range(1, n):
    for j in range(i+1):
        if j == 0: #가장 안쪽 탐색
            arr[i][j] = arr[i][j] + arr[i - 1][j]
        elif i == j: # 가장 바깥쪽 탐색
            arr[i][j] = arr[i][j] + arr[i - 1][j - 1]
        else: #내부 탐색
            arr[i][j] = max(arr[i - 1][j - 1], arr[i - 1][j]) + arr[i][j]
print(max(arr[n - 1]))