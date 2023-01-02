from collections import deque


def bfs(l, sx, sy, lx, ly):
    graph = [[0]*l for _ in range(l)]

    q = deque()
    q.append((sx, sy))
    dx = [-1, -2, -2, -1, 1, 2, 2, 1]
    dy = [2, 1, -1, -2, -2, -1, 1, 2]

    while q:
        x, y = q.popleft()
        for i in range(8):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0 <= nx < l and 0 <= ny < l:
                if graph[nx][ny] == 0:
                    graph[nx][ny] = graph[x][y] + 1
                    if nx == lx and ny == ly:
                        return graph[nx][ny]
                    q.append((nx, ny))


n = int(input())
for _ in range(n):
    l = int(input())
    sx, sy = map(int, input().split())
    lx, ly = map(int, input().split())
    if sx == lx and sy == ly:
        print(0)
    else:
        print(bfs(l, sx, sy, lx, ly))
