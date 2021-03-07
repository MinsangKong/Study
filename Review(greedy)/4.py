#https://www.acmicpc.net/problem/5545
#백준 5545번 최고의 피자(그리디)
n = int(input()) #토핑의 종류
a, b = map(int, input().split()) #도우의 가격, 토핑의 가격
c = int(input()) #도우의 열량
kcal = []
for i in range(n):
    kcal.append(int(input()))
kcal_c=c//a
kcal.sort(reverse=True)
cnt = 0
result = [0]
for i in range(n):
    cnt+=b
    total_cost = a+cnt
    total_kcal = kcal[i]+sum(result)+c
    if kcal_c <= total_kcal//total_cost:
        result.append(kcal[i])
        kcal_c=total_kcal//total_cost
    else :
        break
print(kcal_c)