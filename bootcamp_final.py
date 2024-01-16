def find_prime(x):
    is_prime=True
    for i in range(2,x):
        if x%i==0:
            is_prime=False
            break
    return is_prime


a,b=map(int,input().split())
if a>b:
    (a,b)=(b,a)
for i in range(a,b+1):
    if find_prime(i):
        print(i,end=',')

