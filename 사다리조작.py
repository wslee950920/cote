from itertools import combinations

N, M, H=map(int, input().split(' '))

lst=[]
for _ in range(M):
    lst.append(list(map(int, input().split(' '))))

graph=[[0]*(N+1) for _ in range(H+1)]
for a, b in lst:
    graph[a][b]=b+1
    graph[a][b+1]=b
#print(graph)

cdts=[]
for a in range(1, H+1):
    for b in range(1, N):
        if [a, b] in lst or [a, b+1] in lst or [a, b-1] in lst:
            continue

        cdts.append([a, b])
#print(cdts)

def move(grph, i, a, b):
    rst=True

    if a>H:
        if i==b:
            return True

        else:
            return False

    if grph[a][b]==0:
        rst=rst and move(grph, i, a+1, b)

    else:
        rst=rst and move(grph, i, a+1, grph[a][b])

    return rst

for n in range(0, 4):
    cbns=list(combinations(cdts, n))
    #print(cbns)

    for cbn in cbns:
        for a, b in cbn:
            if graph[a][b]!=0 or graph[a][b+1]!=0:
                break

            graph[a][b]=b+1
            graph[a][b+1]=b

        else:
            for i in range(1, N+1):
                if not move(graph, i, 1, i):
                    break

            else:
                print('answer', n, graph)
            
                exit()

        for a, b in cbn:
            graph[a][b]=0
            graph[a][b+1]=0

print(-1)