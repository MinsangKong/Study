import sys
input = sys.stdin.readline
import copy

text = input().rstrip()
length = len(text)

result = []
temp = copy.deepcopy(text)
resultText = ""
while True:
    tem = ""
    start = temp.find('[')
    end = temp.find(']')
    nums = []
    if start == -1:
        break
    resultText+=temp[:start+2]
    for i in temp[start+2:end-1]:
        if i == ',':
            if tem not in result:
                result.append(tem)
                num = len(result)
                nums.append(num)
            else:
                num = result.index(tem)+1
                nums.append(num)
            tem = ""
        elif i == ' ':
            continue
        else:
            tem+=i
    if tem not in result:
        result.append(tem)
        num = len(result)
        nums.append(num)
    else:
        num = result.index(tem)+1
        nums.append(num)
    nums.sort()
    for i in range(len(nums)):
        resultText+=str(nums[i])
        if i == len(nums)-1:
            resultText+=' ]'
        else:
            resultText+=", "
    temp = temp[end+1:]

print(resultText)
for i in range(len(result)):
    print("[%d] %s" %(i+1, result[i]))
