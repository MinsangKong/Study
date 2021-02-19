#https://www.acmicpc.net/problem/1463
#백준 1463번 1로 만들기(2)
x = int(input())
d = [0]*1000001
d[2] = 1
d[3] = 1
for i in range(4,x+1):
    if i%3 == 0 and i%2 ==0:
        d[i]=min(min(d[i//3], d[i//2]), d[i-1])+1
    elif i%3 == 0:
        d[i]=min(d[i//3],d[i-1])+1
    elif i%2 == 0:
        d[i]=min(d[i//2],d[i-1])+1
    else:
        d[i]=d[i-1]+1
print(d[x])