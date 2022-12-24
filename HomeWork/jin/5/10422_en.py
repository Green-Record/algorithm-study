T = int(input())
L = []
for i in range(T):
    num = int(input())
    if num % 2 != 0:
        L.append(0)
    else:
        L.append(num//2)

# 카탈란 수 리스트
cat = [1, 1, 2]
for i in range(3, max(L)+1):
    newCat = cat[i-1]*(2*i-1)*2/(i+1)
    cat.append(int(newCat) % 1000000007)

for i in L:
    if i == 0:
        print(0)
    else:
        print(cat[i])
