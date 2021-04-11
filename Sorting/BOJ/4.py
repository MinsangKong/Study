#https://www.acmicpc.net/problem/11399
#백준 11399번 ATM(정렬)
n = int(input())
line = list(map(int, input().split()))

line.sort()
cost = 0
result = 0
for i in line:
    cost+=i
    result+=cost
    
print(result)