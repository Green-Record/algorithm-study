import sys
input = sys.stdin.readline
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
sum_arr = [[0]*(n+1) for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(1, n+1):
        sum_arr[i][j] = arr[i-1][j-1]+sum_arr[i-1][j] + \
            sum_arr[i][j-1]-+sum_arr[i-1][j-1]

for _ in range(m):
    x0, y0, x1, y1 = list(map(int, input().split()))
    print(sum_arr[x1][y1]-sum_arr[x1][y0-1] -
          sum_arr[x0-1][y1]+sum_arr[x0-1][y0-1])
