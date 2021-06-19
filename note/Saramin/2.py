import sys
input = sys.stdin.readline

l = int(input())
low = list(input().rstrip())
mid = list(input().rstrip())
high = list(input().rstrip())

lowbit = []
midbit = []
highbit = []

num = ""
for i in low:
    if i !='-':
        num += i
    else:
        lowbit.append(int(num))
        num = ""
lowbit.append(int(num))
num = ""
for i in mid:
    if i !='-':
        num += i
    else:
        midbit.append(int(num))
        num = ""
midbit.append(int(num))
num = ""
for i in high:
    if i !='-':
        num += i
    else:
        highbit.append(int(num))
        num = ""
highbit.append(int(num))

result = [[] for _ in range(l)]
total = 0

for i in range(l):
    num1 = abs(highbit[i]-midbit[i])
    num2 = midbit[i]-lowbit[i]
    num3 = highbit[i]-lowbit[i]
    if num1 != 0 and num1 not in result[i]:
        result[i].append(num1)
    if num2 != 0 and num2 not in result[i]:
        result[i].append(num2)
    if num3 != 0 and num3 not in result[i]:
        result[i].append(num3)
    total += len(result[i])
print(result)
print(total)