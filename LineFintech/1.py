
def count(queries):
    cnt = 0
    for query in queries:
        if query in word :
            print(query)
            cnt += 1
    return cnt

word = dict()
A = dict()
B = dict()


for i in range(1,199):
    key = 'AA'+'B'*i
    word[key] = 1
    A[key] = 1

for i in range(1,198):
    key = 'BA'+'B'*i+'A'
    word[key] = 1
    B[key] = 1
caseA = sorted(A.keys(), key = lambda x : len(x))
caseB = sorted(B.keys(), key = lambda x : len(x))
for a in caseA :
    for b in caseB :
        if len(a)+len(b) > 200 :
            break
        word[a+b] = 1
        word[b+a] = 1

print(count(["AABAAA","BABABB","BABBAAAB","BABAAABAABBABBA"]))