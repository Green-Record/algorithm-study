import heapq

n = int(input())
li = []

for _ in range(n):
    inp = list(map(int,input().split()))
    for i in inp:
        if len(li)<n:
            heapq.heappush(li,i)
        else:
            if li[0]<i:
                heapq.heappush(li,i)
                heapq.heappop(li)
print(li[0])