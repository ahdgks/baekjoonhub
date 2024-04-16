M=int(input())
N=int(input())
num_list=[]
num_len=0
def count_num(num):
    if num < 2:
        return False
    for i in range(2,int(num**0.5)+1):
        if num%i ==0:
            return False
    return num


for i in range(M,N+1):
    num_len+=count_num(i)
    num_list.append(count_num(i))
if num_len==0:
    print(-1)
else:
    print(num_len)
    for number in num_list:
        if number != False:
            print(number)
            break
    
