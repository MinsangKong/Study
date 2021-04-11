#https://www.acmicpc.net/problem/1300 k번째 수
n = int(input()) #가장 직관적인 해결법 but 메모리 초과
k = int(input())
arr = []

for i in range(n):
    for j in range(n):
        arr.append((i+1)*(j+1))

arr.sort()
print(arr[k])
