info=[0,0,1,1,1,0,1,0,1,0,1,1]
edges=[[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]

from collections import defaultdict

def solution(info, edges):
    answer = 0
    
    dd=defaultdict(list)
    for parent, child in edges:
        dd[parent].append(child)
    print(dd)
    
    sheep=[1 if i==0 else 0 for i in info]
    wolves=info[:]
    print(sheep, wolves)
    
    def dfs(parent, siblings):
        nonlocal sheep, wolves
        
        print(parent, siblings)
        
        children=dd[parent]+siblings
        print(children, sheep, wolves)
        
        for i, child in enumerate(children):
            if sheep[child]+sheep[parent]>wolves[child]+wolves[parent]:
                sheep[child]+=sheep[parent]
                wolves[child]+=wolves[parent]  
            
                dfs(child, children[:i]+children[i+1:])
                
                sheep[child]-=sheep[parent]
                wolves[child]-=wolves[parent]
    dfs(0, [])
    print(sheep, wolves)
    
    return answer
solution(info, edges)