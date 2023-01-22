from heapq import heappush, heappop

def solution(operations):
    max_heap = []
    min_heap = []
    for operation in operations:
        if operation == "D 1":
            if max_heap:
                heappop(max_heap)
                if not max_heap or -max_heap[0] < min_heap[0]:
                    min_heap = []
                    max_heap = []
        elif operation == "D -1":
            if min_heap:
                heappop(min_heap)
                if not min_heap or -max_heap[0] < min_heap[0]:
                    max_heap = []
                    min_heap = []
        elif operation[0]=='I':
            num = int(operation[2:])
            heappush(max_heap, -num)
            heappush(min_heap, num)
    if not min_heap:
        return [0, 0]
    return [-heappop(max_heap), heappop(min_heap)]