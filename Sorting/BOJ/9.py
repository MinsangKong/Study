#https://www.acmicpc.net/problem/1764
#백준 1764번 듣보잡(정렬)
n , m = map(int,input().split())
h_num = set()
s_num = set()

for _ in range(n):
    h_num.add(input())
for _ in range(m):
    s_num.add(input())

result = sorted(list(h_num & s_num))
print(len(result))

for i in result:
    print(i)