import sys
input = sys.stdin.readline

n, m = map(int, input().split())
maze = [list(map(int, input().rstrip())) for _ in range(n)]

from collections import deque

def bfs():
  q=deque([(0, 0)])
  while q:
    x, y = q.popleft()
    if x == m-1 and y == n-1:
      return maze[y][x]
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    for i in range(4):
      nx = x+dx[i]
      ny = y+dy[i]

      if 0<=ny<n and 0<=nx<m:
        if maze[ny][nx] == 1:
          maze[ny][nx] = maze[y][x] + 1
          q.append((nx, ny))

print(bfs())