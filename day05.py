#copy,deepcopy 질문
import copy
subject=[1,[2],3]
a=subject
b=subject[:]
c=subject.copy()
d=copy.deepcopy(subject)
print(subject,a,b,c,d)
print(id(subject),id(a),id(b),id(c),id(d))
subject[1]=[0]
print(subject,a,b,c,d)
print(id(subject),id(a),id(b),id(c),id(d))


#질문

def squares(*n): #parameter type:typle
    return [i**2 for i in n] #n은 typle

def run_function(func,*n): # function, parameter type:typle
    return func(*n) #return type:list

print(run_function(squares,1,2,3))

parameter의 개수를 특정 짓기 쉽지 않을 때...
*(애스터리스크)는 여러 arguement를 튜플로 모아서 parameter 전달하는 역할?
다른 함수로 전달된 다음에 *을 풀면 원래대로 여러개의 aurguemt가 나오나??


def gogo(args):
    print(args) # *의 유무..
gogo((1,2,3,4)) #arguement type tuple


def gogo(*args):
    print(*args) # *의 유무..
gogo(1,2,3,4) #arguement type tuple



def print_args(a,b,*args):
    print(a)
    print(b)
    print('positinal tuple',args)
# print_args(5,4,3,2,1)

a=[1,2,3,4]
print(*a) #원소 출력하는 것이랑 뭐가 다르지??
#


def my_range(first=0,last=5,step=1):
    number=first
    while number<last:
        yield number
        number+=step
r=my_range()
print(r,type(r))

for x in r:
    print(x)

for x in r:
    print(x)

def document_it(func):
    def new_function(*args,**kwargs):
        print('Running function:',func.__name__)
        print('positional:',args)
        print('Keyword argument:',kwargs)
        print(type(args))

        result=func(*args,**kwargs)
        print('Result:',result)
        return result
    return new_function

def add_ints(a,b):
    return a+b

cooler_add_ints=document_it(add_ints)
print(cooler_add_ints)
cooler_add_ints(3,5,) #new function

# arg는 튜이기 때문에 add_ints()의 arguement로 부적절
#->*을 통해서 unpacking을 하는 것 아닌가









