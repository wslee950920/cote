from collections import defaultdict

N=int(input())
people=[0]+list(map(int, input().split(' ')))
dd=defaultdict(list)

for n in range(1, N+1):
    tmp=list(map(int, input().split(' ')))

    for i in range(1, tmp[0]+1):
        dd[n].append(tmp[i])
print(N, people, dd)

answer=10*100
def connected(parent, target, visited):
    global answer
    #print(parent, target, visited)
    rst=False

    if target in dd[parent]:
        return True

    for child in dd[parent]:
        if child in visited:
            continue

        rst|=connected(child, target, visited+[child])

    return rst
#print(connected(2, 4, [2]))

def dfs(red, blue, parent, visited):
    global answer

    print('a', answer, red, blue)

    if not red or not blue:
        return

    for i in red:
        for j in red:
            if i==j:
                continue

            if not connected(i, j, [i]):
                return

    for i in blue:
        for j in blue:
            if i==j:
                continue

            if not connected(i, j, [i]):
                return

    answer=min(answer, abs(sum([people[r] for r in red])-sum([people[b] for b in blue])))
    print('b', answer, red, blue)
    
    for child in dd[parent]:
        if child in visited:
            continue

        dfs(red+[child], blue-{child}, child, visited+[child])

cities=[i for i in range(1, N+1)]
for i in range(N):
    dfs([cities[i]], set(cities[:i]+cities[i+1:]), cities[i], [cities[i]])
    print(answer)