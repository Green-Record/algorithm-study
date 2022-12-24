def solution(citations):
    citations = sorted(citations, reverse=True)
    l = len(citations)
    for i in range(l):
        if citations[i] <= i:
            return i
    return l
