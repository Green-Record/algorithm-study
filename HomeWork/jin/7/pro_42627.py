import heapq

def solution(jobs):
    l = len(jobs)
    heapq.heapify(jobs)
    current_time = jobs[0][0]
    rs = []
    h = []
    while jobs or h:
        while jobs and jobs[0][0]<=current_time:
            a,b = heapq.heappop(jobs)
            heapq.heappush(h,[b,a])
        if not h:
            current_time = jobs[0][0]
        else:
            a,b = heapq.heappop(h)
            current_time+=a
            rs.append(current_time-b)
    return sum(rs)//l
