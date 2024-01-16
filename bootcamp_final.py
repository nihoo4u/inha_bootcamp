while True:
    a=input()
    if a=='q':
        print('terminate the calculator')
        break
    if int(a)<=1:
        print(f'{int(a)} is not a prime number ')
        break
    is_prime=True
    for i in range(2,int(a)):

        if int(a)%i==0:
            is_prime=False

            break
    if is_prime:
        print(f'{int(a)} is a prime number')
    else:
        print(f'{int(a)}is not a prime number')

