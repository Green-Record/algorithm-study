N = int(input())
budget = list(map(int, input().split()))
M = int(input())

start, end = M//N, max(budget)
total_budget = 0

if sum(budget) <= M:
	print(max(budget))
else:
    while start <= end:
        mid = (start+end) // 2
        total_budget = 0
        for i in budget:
            total_budget+=min(i,mid)
        if total_budget <= M: 
            start = mid + 1
        else: 
            end = mid - 1
    print(end)