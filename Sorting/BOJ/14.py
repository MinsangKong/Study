#https://www.acmicpc.net/problem/1246
#백준 1246번 온라인판매(정렬)
n, m = map(int, input().split())
arr = []
result = 0
cost = 0
max = 0

for i in range(m):
    arr.append(int(input()))
arr.sort()

for i in range(m):
    if m-i < n :
        result = arr[i] * (m-i)
    else:
        result = arr[i] * n
    if max < result:
        cost = arr[i]
        max = result
print(cost, max, sep=' ')