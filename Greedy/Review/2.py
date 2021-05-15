#https://www.acmicpc.net/problem/1449
#백준 1449번 수리공 항승(그리디)
n, l = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()

start = arr[0]
end = arr[0] + l
count = 1
for i in range(n):
    if start <= arr[i] < end:
        continue
    else:
        start = arr[i]
        end = arr[i] + l
        count += 1
print(count)