import heapq as h

def solution(operations):
    answer_max = []
    answer_min = []
    for cmd in operations:
        if cmd[0]=='I':
            h.heappush(answer_max,-int(cmd[2:]))
            h.heappush(answer_min,int(cmd[2:]))
            h.heappush(answer_min,-int(cmd[2:]))
        elif cmd=='D 1' and answer_max:
            h.heappop(answer_max)
            h.heappop(answer_min)
        elif cmd=='D -1' and answer_min:
            h.heappop(answer_min)
        print(cmd,answer_max,answer_min)
    if answer_max and answer_max:
        a=answer_max[0]
        b=answer_min[0]
        if -a>b:
            return [-a,b]
        else:
            return [0,0]
    else:
        return [0,0]

print(solution(["I 4", "I 3", "I 2", "I 1", "D 1", "D 1", "D -1", "D -1", "I 5", "I 6"]))