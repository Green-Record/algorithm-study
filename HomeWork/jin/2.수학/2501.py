n, th = map(int, input().split())
li = []
for i in range(1, n+1):
    if n % i == 0:
        li.append(i)
if th > len(li):
    print(0)
else:
    print(li[th-1])
