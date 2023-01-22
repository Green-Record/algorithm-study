from itertools import combinations

while True:
    inp = list(map(int,input().split()))
    if inp[0]==0:
        break
    a = combinations(inp[1:],6)
    for i in a:
        print(*i)
    print()