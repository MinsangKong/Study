#https://www.acmicpc.net/problem/5021
#백준 5021번 왕위 계승(DFS)
#import sys
#input = sys.stdin.readline
from collections import deque

def find_blood(name):
    if name == king:
        return 1
    if name not in blood:
        return 0
    if not blood[name]:
        return 0
    return (find_blood(blood[name][0])+find_blood(blood[name][1])) / 2
        

n, m = map(int, input().split())

king = input().rstrip()

blood = dict()
for _ in range(n):
    a,b,c = input().split()
    for name in [a,b,c]:
        if name not in blood:
            blood[name] = []
    blood[a] = [b,c]
    
check = []

for _ in range(m):
    check.append(input().rstrip())
    
result = float('-inf')
name = ""

for i in check:
    point = find_blood(i)
    if point > result:
        result = point
        name = i
        
print(name)