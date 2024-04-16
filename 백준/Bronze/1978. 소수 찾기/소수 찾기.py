N = int(input())
number = list(map(int,input().split()))

def count_num(x):
    a=0
    for i in range(1,x+1):
        if x%i == 0:
            a+=1
    if a==2:
        return 1
    return 0
    

len_num=0
for i in number:
    len_num+=count_num(i)
print(len_num)