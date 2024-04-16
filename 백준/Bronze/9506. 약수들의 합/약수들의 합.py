while True:
    num=0
    num_list=[]
    a=int(input())
    if a== -1:
        break
    for i in range(1,a):
        if a%i==0:
            num+=i
            num_list.append(str(i))
    perfect=' + '.join(num_list)
    if num ==a:
        print(f'{a} = {perfect}')
    else:
        print(f'{a} is NOT perfect.')