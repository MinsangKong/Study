import sys
read = sys.stdin.readline

N = int(read())
nums = list(map(int, read().split()))
dic = {n: i for i, n in enumerate(sorted(set(nums)))}

print(" ".join(str(dic[n]) for n in nums))
'''
속도 면에서는 for문으로 출력하는 것보다 join문을 활용해서 출력한게 훨씬 빨랐다
'''