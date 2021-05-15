import sys
input = sys.stdin.readline
N = int(input())
dic = {}
for i in range(N):
    a, b = map(int, input().split())
    dic[a] = b
s = sorted(dic.keys())
l = [s[0], dic[s[0]]]
sol = 0

for i in s[1:]:
    if l[1] < i:
        sol += l[1]-l[0]
        l = [i, dic[i]]
    else:
        if l[1] < dic[i]:
            l[1] = dic[i]

sol += l[1]-l[0]
print(sol)
'''
가장 빠르게 문제를 해결하기 위해서는 값을 입력받을 때 dic를 활용하면서
if문의 조건을 좀 더 간소화 해서 문제를 풀어야 한다.
'''