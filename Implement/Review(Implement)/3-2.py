#https://www.acmicpc.net/problem/7568
#백준 7568번 덩치(구현)
num=int(input())
val=[]
for i in range(num) :
    val.append(list(map(int,input().split())))

for i in val :
    rank=1
    for j in val :
        if i[0] < j[0] and i[1] < j[1]:
                rank += 1
    print(rank,end=' ')
'''
알고리즘은 동일하지만 출력을 바로바로 안해줬다고 속도차이가 58ms와 72ms로 컸다.
'''