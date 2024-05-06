import bisect
T= int(input())

for _ in range(T):
    cnt=0
    N,M = map(int,input().split())
    A=list(map(int,input().split()))
    B=list(map(int,input().split()))
    B.sort()
    for a in A:
        pos = bisect.bisect_left(B,a)
        cnt+=pos
    print(cnt)