#https://www.acmicpc.net/problem/11055
#백준 11055번 가장 큰 증가 부분 수열
n = int(input())
arr = list(map(int, input().split()))
d = [0] * n
d[0] = arr[0]
for i in range(1, n):
    s = []
    for j in range(i - 1, -1, -1):
        if arr[i] > arr[j]:
            s.append(d[j])
    if not s:
        d[i] = arr[i]
    else:
        d[i] = arr[i] + max(s)
print(max(d))