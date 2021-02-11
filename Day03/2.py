#https://www.acmicpc.net/problem/1764 듣보잡
n, m = map(int, input().split()) #시간초과 발생
h_num = []
s_num = []

for i in range(n):
    h_num.append(input())
for j in range(m):
    s_num.append(input())
    
result = []
for i in h_num:
    if i in s_num:
        result.append(i)
result.sort()
print(len(result))
for i in result:
    print(i)