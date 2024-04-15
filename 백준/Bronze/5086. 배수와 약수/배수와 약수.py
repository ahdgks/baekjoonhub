while True:
    a,b= map(int,input().split())
    if (a,b) == (0,0):
        break
    if (b%a==0)&(a<b):
        print('factor')
    elif (a%b==0)&(b<a):
        print('multiple') 
    else:
        print('neither') 