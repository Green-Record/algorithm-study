def solution(numbers):
    n = sorted(numbers,key=lambda x:str(x)*3,reverse=True)
    return str(int(''.join(map(str,n))))