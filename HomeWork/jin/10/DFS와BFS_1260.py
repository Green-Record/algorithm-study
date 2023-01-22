from collections import deque

v, e, s = map(int,input().split())

array = [[] for _ in range(v+1)]
for i in range(e):
    a, b = map(int,input().split())
    array[a].append(b)
    array[b].append(a)

for i in array:
    i.sort()

def dfs(s):
    chk[s]=0
    print(s,end=' ')
    for i in array[s]:
        if i and chk[i]:
            dfs(i)
            
def bfs(s):
    q = deque([s])
    chk[s]=0
    while q:
        s = q.popleft()
        print(s,end=' ')
        for i in array[s]:
            if i and chk[i]:
                q.append(i)
                chk[i]=0
                
chk=[1]*(v+1)
dfs(s)
print()
chk=[1]*(v+1)
bfs(s)
                