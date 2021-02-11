# https://www.acmicpc.net/problem/1789 수들의 합
s = int(input()) #1~p까지의 합이 s보다 클 경우 1~p-1에서 가장 큰 수 
sum = 1 #부터 1씩 더해주면 겹치지 않고 s까지 도달할 수 있다.
p=1    
arr = [1]
while sum < s:
    p+=1
    sum+=p
    if sum <= s:
        arr.append(p)
print(len(arr)) #굳이 1씩 안더하더라도, 1~p-1까지의 길이가 가장 큰 n이 된다