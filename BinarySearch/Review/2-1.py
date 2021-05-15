#https://www.acmicpc.net/problem/17266
#백준 17266번 어두운 굴다리(이분 탐색)
#import sys
#input = sys.stdin.readline
def check(light, mid):
    if light[1]-light[0] > mid:
        return False
    if light[-1]-light[-2] > mid:
        return False
    for i in range(1,len(light)-2):
        if (light[i+1]-light[i])/2 > mid:
            return False
    return True

n = int(input())
m = int(input())
light = [0] + list(map(int, input().split())) + [n]

result = 0
start = 0
end = n
while start <= end:
    mid = (start+end)//2
    if check(light,mid) :
        result = mid
        end = mid-1
    else:
        start = mid+1     
print(result)
'''
절대 실버5 수준 문제가 아니었다. 중간에 있는 가로등사이의 체크를 구현하는게 까다로웠다
경우에 수를 나눈 뒤 구현해서 겨우 답을 구했다. 이분 탐색으로 구현시 체감 난이도는 
골드5 정도 되는 것 같았다. 이분 탐색으로는 엄청 까다로운 문제가 점화식을 세우니까 훨씬 쉬워졌다.
'''