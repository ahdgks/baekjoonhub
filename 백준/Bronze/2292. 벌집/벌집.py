num=0
count=0
i=0
N = int(input())

while num<N:
    if num==0:
        num=1
    else:
        num = (i*6)+num
    i+=1
    count+=1
print(count)