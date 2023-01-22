from collections import deque

dx=[0,-1,1,0]
dy=[1,0,0,-1]

def dfs(x,y): #런타임에러
    array[x][y]=0
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<r and 0<=ny<c and array[nx][ny]==1:
            dfs(nx,ny)
            
def bfs(x,y):
    array[x][y]=0
    q=deque()
    q.append([x,y])
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<r and 0<=ny<c and array[nx][ny]==1:
                array[nx][ny]=0
                q.append([nx,ny])

n = int(input())
for _ in range(n):
    r,c,nn = map(int,input().split())
    array = [[0] * c for _ in range(r)]
    for _ in range(nn):
        a,b = map(int,input().split())
        array[a][b]=1
    cnt=0
    for x in range(r):
        for y in range(c):
            if array[x][y]:
                bfs(x,y)
                # dfs(x,y)
                cnt+=1
    print(cnt)