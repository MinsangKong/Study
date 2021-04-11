#https://www.acmicpc.net/problem/11650
#백준 11650번 좌표 정렬하기(정렬)
n = int(input())
arr=[]

for i in range(n):
    arr.append(list(map(int, input().split())))

u = lambda x : (x[0], x[1])
arr = sorted(arr, key = u)
for i in arr:
    print(i[0], i[1], sep=' ')