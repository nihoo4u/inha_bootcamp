#4:구간소,3:소수 판정프로그램수1번 화씨 to 섭
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
        x=int(input())
        is_prime=True
        for i in range(2,x):
            if x%i==0:
                is_prime=False
                break
        if is_prime:
            print(f'{x} is a prime number')
        else:
            print(f'{x} is not a prime number')
    else:
        a,b=map(int,input().split())

        if a>b:
            a,b=b,a
        for i in range(a+1,b):
            is_prime = True
            for j in range(2,i):
                if i%j==0:
                    is_prime=False
                    break

            if is_prime:
                print(i,end=' ')






# 6.1
l=[3,2,1,0]
for i in l:
    print(i,end=' ')

# 6.2
guess_me=7
number=1
while True:
    if number<guess_me:
        print('too low')

    elif number==guess_me:
        print('found it')
        break
    else:
        print('Oops')
        break
    number+=1

print(number)

6.3
guess_me=5
for number in range(10):
    if number<guess_me:
        print('too low')
    elif number==guess_me:
        print('found it')
        break
    else:
        print('Oops')
        break