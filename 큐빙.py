from copy import deepcopy

m=int(input())

lst=[]
for _ in range(m):
    n=int(input())
    lst.append(list(input().split(' ')))

cube=dict()
cube['U']=[['w']*3 for _ in range(3)]
cube['u']=list(map(list, zip(*cube['U'])))
cube['D']=[['y']*3 for _ in range(3)]
cube['d']=list(map(list, zip(*cube['D'])))
cube['F']=[['r']*3 for _ in range(3)]
cube['f']=list(map(list, zip(*cube['F'])))
cube['B']=[['o']*3 for _ in range(3)]
cube['b']=list(map(list, zip(*cube['B'])))
cube['L']=[['g']*3 for _ in range(3)]
cube['l']=list(map(list, zip(*cube['L'])))
cube['R']=[['b']*3 for _ in range(3)]
cube['r']=list(map(list, zip(*cube['R'])))

for tc in lst:
    dcp=deepcopy(cube)
    
    for s, d in list(tc):
        if d=='+':
            if s=='U':
                dcp['B'][2], dcp['R'][0], dcp['F'][0], dcp['L'][0]=dcp['L'][0], dcp['B'][2], dcp['R'][0], dcp['F'][0]
                dcp['b']=list(map(list, zip(*dcp['B'])))
                dcp['r']=list(map(list, zip(*dcp['R'])))
                dcp['f']=list(map(list, zip(*dcp['F'])))
                dcp['l']=list(map(list, zip(*dcp['L'])))

            elif s=='D':
                dcp['F'][2], dcp['L'][2], dcp['B'][0], dcp['R'][2]=dcp['L'][2], dcp['B'][0], dcp['R'][2], dcp['F'][2]
                dcp['u']=list(map(list, zip(*dcp['U'])))
                dcp['D']=list(map(list, zip(*dcp['d'])))
                dcp['R']=list(map(list, zip(*dcp['r'])))
                dcp['L']=list(map(list, zip(*dcp['l'])))

            elif s=='F':
                dcp['U'][2], dcp['r'][0], dcp['D'][0], dcp['l'][2]=dcp['l'][2], dcp['U'][2], dcp['r'][0], dcp['D'][0]
                dcp['u']=list(map(list, zip(*dcp['U'])))
                dcp['D']=list(map(list, zip(*dcp['d'])))
                dcp['R']=list(map(list, zip(*dcp['r'])))
                dcp['L']=list(map(list, zip(*dcp['l'])))

            elif s=='B':
                dcp['U'][0], dcp['l'][0], dcp['D'][2], dcp['r'][2]=dcp['r'][2], dcp['U'][0], dcp['l'][0], dcp['D'][2]
                dcp['u']=list(map(list, zip(*dcp['U'])))
                dcp['L']=list(map(list, zip(*dcp['l'])))
                dcp['d']=list(map(list, zip(*dcp['D'])))
                dcp['R']=list(map(list, zip(*dcp['r'])))

            elif s=='L':
                dcp['u'][0], dcp['f'][0], dcp['d'][0], dcp['b'][0]=dcp['b'][0], dcp['u'][0], dcp['f'][0], dcp['d'][0]
                dcp['U']=list(map(list, zip(*dcp['u'])))
                dcp['F']=list(map(list, zip(*dcp['f'])))
                dcp['D']=list(map(list, zip(*dcp['d'])))
                dcp['B']=list(map(list, zip(*dcp['b'])))

            elif s=='R':
                dcp['b'][2], dcp['d'][2], dcp['f'][2], dcp['u'][2]=dcp['u'][2], dcp['b'][2], dcp['d'][2], dcp['f'][2]
                dcp['R']=list(map(list, zip(*dcp['r'])))
                dcp['D']=list(map(list, zip(*dcp['d'])))
                dcp['F']=list(map(list, zip(*dcp['f'])))
                dcp['U']=list(map(list, zip(*dcp['u'])))

        elif d=='-':
            if s=='U':
                dcp['L'][0], dcp['F'][0], dcp['R'][0], dcp['B'][2]=dcp['B'][2], dcp['L'][0], dcp['F'][0], dcp['R'][0]
                dcp['b']=list(map(list, zip(*dcp['B'])))
                dcp['r']=list(map(list, zip(*dcp['R'])))
                dcp['f']=list(map(list, zip(*dcp['F'])))
                dcp['l']=list(map(list, zip(*dcp['L'])))

            elif s=='D':
                dcp['L'][2], dcp['B'][0], dcp['R'][2], dcp['F'][2]=dcp['F'][2], dcp['L'][2], dcp['B'][0], dcp['R'][2]
                dcp['l']=list(map(list, zip(*dcp['L'])))
                dcp['b']=list(map(list, zip(*dcp['B'])))
                dcp['r']=list(map(list, zip(*dcp['R'])))
                dcp['f']=list(map(list, zip(*dcp['F'])))

            elif s=='F':
                dcp['l'][2], dcp['D'][0], dcp['r'][0], dcp['U'][2]=dcp['U'][2], dcp['l'][2], dcp['D'][0], dcp['r'][0]
                dcp['L']=list(map(list, zip(*dcp['l'])))
                dcp['d']=list(map(list, zip(*dcp['D'])))
                dcp['R']=list(map(list, zip(*dcp['r'])))
                dcp['u']=list(map(list, zip(*dcp['U'])))

            elif s=='B':
                dcp['r'][2], dcp['D'][2], dcp['l'][0], dcp['U'][0]=dcp['U'][0], dcp['r'][2], dcp['D'][2], dcp['l'][0]
                dcp['R']=list(map(list, zip(*dcp['r'])))
                dcp['d']=list(map(list, zip(*dcp['D'])))
                dcp['L']=list(map(list, zip(*dcp['l'])))
                dcp['u']=list(map(list, zip(*dcp['U'])))

            elif s=='L':
                dcp['u'][0], dcp['f'][0], dcp['d'][0], dcp['b'][0]=dcp['f'][0], dcp['d'][0], dcp['b'][0], dcp['u'][0]
                dcp['U']=list(map(list, zip(*dcp['u'])))
                dcp['F']=list(map(list, zip(*dcp['f'])))
                dcp['D']=list(map(list, zip(*dcp['d'])))
                dcp['B']=list(map(list, zip(*dcp['b'])))

            elif s=='R':
                dcp['u'][2], dcp['f'][2], dcp['d'][2], dcp['b'][2]=dcp['b'][2], dcp['u'][2], dcp['f'][2], dcp['d'][2]
                dcp['U']=list(map(list, zip(*dcp['u'])))
                dcp['F']=list(map(list, zip(*dcp['f'])))
                dcp['D']=list(map(list, zip(*dcp['d'])))
                dcp['B']=list(map(list, zip(*dcp['b'])))
        print(s, d, dcp)
    print(dcp['U'])