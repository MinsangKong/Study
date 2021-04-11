#https://www.acmicpc.net/problem/1026
#백준 1026번 보물(정렬)
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
s = 0
a.sort()

for i in range(len(a)):
    b_max = 0
    for j in range(len(b)):
        if b[j] > b_max:
            b_max = b[j]
    s = s+(b_max*a[i])
    b.remove(b_max)
print(s)
