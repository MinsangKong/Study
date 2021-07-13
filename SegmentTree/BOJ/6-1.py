#https://www.acmicpc.net/problem/2517
#백준 2517번 달리기(세그먼트 트리)
#import sys
#input = sys.stdin.readline

def update(idx, value):
    while idx < n:
        trees[idx] += value
        idx |= idx+1
        
def sub_sum(idx):
    temp = 0
    while idx >= 0:
        temp += trees[idx]
        idx = (idx&(idx+1))-1
    return temp
        
n = int(input())

powers = [(int(input()),i) for i in range(n)]
idx = 0
scores = [0]*n

for data,i in sorted(powers): #상대적인 순위로 변환
    scores[i] = idx 
    idx+=1
    
trees = [0]*n

for i, score in enumerate(scores):
    print(i+1-sub_sum(score))
    update(score, 1)
'''
흐름을 알것도 같은데 풀 자신이 없다...
'''