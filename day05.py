# import copy
# subject=[1,[2],3]
# a=subject
# b=subject[:]
# c=subject.copy()
# d=copy.deepcopy(subject)
# print(subject,a,b,c,d)
# print(id(subject),id(a),id(b),id(c),id(d))
# subject[1]=[0]
# print(subject,a,b,c,d)
# print(id(subject),id(a),id(b),id(c),id(d))

# def print_args(a,b,*args):
#     print(a)
#     print(b)
#     print('positinal tuple',args)
# # print_args(5,4,3,2,1)
#
# a=[1,2,3,4]
# print(*a) #원소 출력하는 것이랑 뭐가 다르지??


# def print_data(data,*,start=0,end=100):
#     for value in (data[start:end]):
#         print(value)
# data=['a','b','c','d','e','f']
# print_data(data)

# def print_kwargs(**kwargs):
#     print(kwargs)
# print_kwargs(wine="df",gogo="sdf")

def squares(*n): #parameter type:typle
    return [i**2 for i in n]

def run_function(func,*n): # function, parameter type:typle
    return func(*n) #return type:list
print(squares(1,2,3))
print(run_function(squares,1,2,3))

# def sum_args(*args):
#     return sum(args)
# def run_with(func,*args):
#     return func(args)


