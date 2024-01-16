while True:
    a=input()
    if a=='q':
        print('terminate the calculator')
        break
    s=0
    for i in range(2,int(a)):

        if int(a)%i==0:
            print(f'{int(a)} is not a prime number ')
            break
        s+=1
    if s==int(a)-2:
        print(f'{int(a)} is a prime number')







