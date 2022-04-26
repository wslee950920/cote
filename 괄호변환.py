from collections import Counter

def solution(p):
    answer = ''
    
    dic=dict()
    dic['(']=')'
    dic[')']='('
    
    def check(s):
        stack=[]
        
        for c in s:
            if not stack:
                stack.append(c)
                
                continue
                
            if c==')' and stack[-1]=='(':
                stack.pop()
                
            else:
                stack.append(c)
                
        return not stack
    
    def func(w):       
        u=[]
        v=[]
                
        i=0
        while i<len(w):
            u.append(w[i])
            i+=1
            
            cnt=Counter(u)
            if cnt['(']==cnt[')']:
                v=w[i:]
                
                break
        print(u, v)
        
        if check(u):
            return u+func(v[:])
            
        else:
            return ['(']+func(v[:])+[')']+[dic[c] for c in u[1:-1]]
    func(list(p))           

p="(()())()"
solution(p)