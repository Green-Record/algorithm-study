from collections import deque
def solution(maps):
    n, m = len(maps), len(maps[0])
    q = deque()
    q.append((0, 0))
    
    dx=[0, 0, 1, -1]
    dy=[1, -1, 0, 0]
    
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<m:
                if maps[nx][ny] == 1:
                    maps[nx][ny] = maps[x][y] +1
                    if nx == n-1 and ny == m-1:
                        return maps[nx][ny]
                    q.append((nx, ny))
                    
    return -1