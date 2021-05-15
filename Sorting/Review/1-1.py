#https://www.acmicpc.net/problem/10814
#백준 10814번 나이순 정렬(정렬)
#import sys
#input = sys.stdin.readline

n = int(input())
arr = []

for i in range(n):
    data = list(input().split())
    arr.append((int(data[0]),data[1],i))

arr.sort(key = lambda x : (x[0],x[2],x[1]))

for i in arr:
    print(i[0],i[1], sep=' ')