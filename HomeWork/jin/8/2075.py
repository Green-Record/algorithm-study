n = int(input())
li = [list(map(int, input().split())) for _ in range(n)]

rs = sorted(sum(li, []), reverse=True)
print(rs[n-1])
