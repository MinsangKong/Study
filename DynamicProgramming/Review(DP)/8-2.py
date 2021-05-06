import sys

t = int(sys.stdin.readline())
nList = []
for i in range(t):
    nList.append(int(sys.stdin.readline()))

ansList1 = [0, 1, 0, 1] + [0]*(max(nList)-3)
ansList2 = [0, 0, 1, 1] + [0]*(max(nList)-3)
ansList3 = [0, 0, 0, 1] + [0]*(max(nList)-3)

for i in range(4, max(nList)+1):
    ansList1[i] = (ansList2[i-1] + ansList3[i-1]) % 1000000009
    ansList2[i] = (ansList1[i-2] + ansList3[i-2]) % 1000000009
    ansList3[i] = (ansList1[i-3] + ansList2[i-3]) % 1000000009

for n in nList:
    print((ansList1[n] + ansList2[n] + ansList3[n])%1000000009)
'''
시간 효율을 극대화 하기 위해서는 testcase를 입력 받을 때 한 번에 받은 뒤 그 중에서 가장
큰 값을 최대값으로 해서 dp를 구하면 더 빠르게 구할 수 있다.
'''