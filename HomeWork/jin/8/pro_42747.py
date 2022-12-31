def solution(citations):
    answer = 0
    n=len(citations)

    for i in range(max(citations),min(citations)-1,-1):
        k=[j for j in citations if j>=i]
        if len(k)>=i:
            return i
    return len(k)