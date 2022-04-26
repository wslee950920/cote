from itertools import combinations
import math

N=int(input())

S=[]
for _ in range(N):
    S.append(list(map(int, input().split(' '))))

answer=math.inf

lst=list(combinations([n for n in range(N)], N//2))
for i in range(len(lst)//2):
    start=set(lst[i])
    link=set([n for n in range(N)])-start
    #print(start, link)

    s1=0
    for i, j in list(combinations(start, 2)):
        s1+=S[i][j]
        s1+=S[j][i]

    s2=0
    for i, j in list(combinations(link, 2)):
        s2+=S[i][j]
        s2+=S[j][i]

    diff=abs(s1-s2)
    answer=min(answer, diff)
print(answer)