#https://www.acmicpc.net/problem/16500
#백준 16500번 문자열 판별
s = input()
n = int(input())
arr = []
for i in range(n):
    arr.append(input())
    
d = [0]* 101

for i in range(len(s) - 1, -1, -1):
    for a in arr:
        if d[i] == 1:
            break
        if i+len(a) == len(s): #끝에서부터 시작해서 일치하면 계속 1을 전달하는 구조
            if s[i:i+len(a)] == a:
                d[i] = 1
        elif i+len(a) < len(s):
            if s[i:i+len(a)] == a:
                d[i] = d[i+len(a)]#끝까지 다 일치하면 d[0]에는 1이 들어감

print(d[0])