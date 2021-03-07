#https://www.acmicpc.net/problem/20115
#백준 20115번 에너지 드링크(그리디)
n = int(input())
drink = list(map(int, input().split()))
drink.sort(reverse=True)

result = drink[0]
for i in range(1,n):
    result += (drink[i]/2)
if result == int(result):
    print(int(result))
else:
    print(result)