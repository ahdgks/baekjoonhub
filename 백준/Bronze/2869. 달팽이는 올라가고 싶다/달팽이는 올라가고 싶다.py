height=0
day=0
A,B,V=map(int,input().split())

rest=V-A
up = A-B

if rest < 0:
    print(1)
else:
    if rest%up==0:
        print(rest//up+1)
    else:
        print(rest//up+2)