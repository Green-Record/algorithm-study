n, d, k, c = map(int,input().split())
li = [int(input()) for _ in range(n)]
li2 = li*2
rs = 0
for i in range(n):
    setV = set(li2[i:i+k]+[c])
    rs = max(rs,len(setV))
print(rs)