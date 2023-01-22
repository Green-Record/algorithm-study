from collections import deque
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

v, e = map(int,input().split())
array = [[] for _ in range(v+1)]


for _ in range(e):
    a,b = map(int,input().split())
    array[a].append(b)
    array[b].append(a)

def dfs(n):
    if chk[n]:
        chk[n]=0
    for i in array[n]:
        if chk[i]:
            dfs(i)
            
def bfs(n):
    q=deque()
    q.append(n)
    chk[n]=0
    while q:
        n = q.popleft()
        for i in array[n]:
            if chk[i]:
                chk[i]=0
                q.append(i)

cnt=0
chk = [1] * (v+1)
for i in range(1,v+1):
    if chk[i]:
        bfs(i)
        cnt+=1
print(cnt)

# cnt=0
# chk = [1] * (v+1)
# for i in range(1,v+1):
#     if chk[i]:
#         bfs(i)
#         cnt+=1
# print(cnt)
