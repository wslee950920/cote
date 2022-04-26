N=int(input())

plan=[None]
for _ in range(N):
    plan.append(list(map(int, input().split(' '))))

answer=0

def dfs(today, tot):
    global answer
    answer=max(answer, tot)

    #print(today, tot)
    for nxt in range(today+1, N+1):
        if today+plan[today][0]<=nxt and nxt+plan[nxt][0]<=N+1:
            dfs(nxt, tot+plan[nxt][1])

for n in range(1, N+1):
    if n+plan[n][0]<=N+1:
        dfs(n, plan[n][1])

print(answer)