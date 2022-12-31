n = int(input())
li = list(int(input()) for _ in range(n))

dp=[li[0]]
if n>1:
    dp.append(li[0]+li[1])
if n>2:
    dp.append(max(li[0]+li[2],li[1]+li[2]))

for i in range (3,n):
    dp.append(max(dp[i-3]+li[i-1]+li[i],dp[i-2]+li[i]))
print(dp[n-1])