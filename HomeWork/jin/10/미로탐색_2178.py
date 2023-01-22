from collections import deque
# import copy

n, m = map(int,input().split())

array2 = [list(map(int,input())) for _ in range(n)]
# array1 = copy.deepcopy(array2)
chk = [[1]*m for _ in range(n)]
dx=[0,-1,1,0]
dy=[1,0,0,-1]

def dfs(x,y):
    chk[x][y]=0
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0<=nx<n and 0<=ny<m and array1[nx][ny]==1 and chk[nx][ny]:
            array1[nx][ny] = array1[x][y]+1
            dfs(nx,ny)

def bfs(x,y):
    q = deque()
    q.append([x,y])
    chk[x][y]=0
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<n and 0<=ny<m and array2[nx][ny]==1 and chk[nx][ny]:
                array2[nx][ny] = array2[x][y]+1
                chk[nx][ny]=0
                q.append([nx,ny])
                
        
# chk = [[1]*m for _ in range(n)]
# dfs(0,0)
bfs(0,0)
# for i in array1:
#     print(i)   
# for i in array2:
#     print(i)   
# print(array1[n-1][m-1])
print(array2[n-1][m-1])

    
