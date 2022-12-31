n = int(input())

li = [int(input()) for _ in range(n)]

dp = [0,1,2,4]
for i in range(4,max(li)+1):
    dp.append(dp[i-1]+dp[i-2]+dp[i-3])

for i in li:
    print(dp[i])
