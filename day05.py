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
a,b=map(int,input().split())
if a>b:
    a,b=b,a
for i in range(a,b):
    if isprime(i):
        print(f'{i} is a prime number')
    else:
        print(f'{i} is not a prime number')
##