def isprime(n)->bool():
    if n<2:
        return False
    else:
        i=2
        while i*i<=n:
            if n%i==0:
                return False
            i+=1
        return True
while True:
    a=int(input())
    if a==5:
        print('Terminate the program')
        break
    if a==1:
        f = float(input('input f'))
        print(f'f:{f} and c:{(f - 32) * 5 / 9:.3f}')
    elif a==2:
        c = float(input('input c'))
        print(f'c:{c} and f:{c * 9 / 5 + 32}')
    elif a==3:
        n=int(input())
        if isprime(n):
            print(f'{n} is a prime number')
        else:
            print(f'{n} is not a prime number')
    else:
        a, b = map(int, input().split())
        if a > b:
            a, b = b, a
        for i in range(a, b):
            if isprime(i):
                print(f'{i} is a prime number')
            else:
                print(f'{i} is not a prime number')
