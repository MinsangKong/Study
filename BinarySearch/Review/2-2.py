n = int(input())
m = int(input())
l = [int(x) for x in input().split()]
max = max(l[0], n - l[-1]) #처음과 끝을 기준으로 했을 때 더 큰 값으로 초기값 지정

for x in range(1, m):
    if (l[x] - l[x - 1]) % 2 == 1:
        t = (l[x] - l[x - 1]) // 2 + 1
    else:
        t = (l[x] - l[x - 1]) // 2
    
    if t > max:
        max = t

print(max)