def solution(citations):
    citations.sort(reverse=True)
    for i in range(len(citations),-1,-1):
        an = [j for j in citations if j>=i]
        if len(an)>=i:
            return i