# a='dfdfdfdf'
# print(a.split('f'))
# b=[1,2,3,4,5,6]
# b=list(map(str,b))
# print('/'.join(b))

# a='asdfsd'
# b=a.replace('a','/',3)
# print(b)

# a=[[0]*5 for _ in range(4)]
# for i in a:
#     print(*i)


# a=[1,4,2,1,5,7,3,3,1,1,2,1,5]
# remove_set=[1,3,5]
# b=[x for x in a if x not in remove_set]
# print(*b,sep='/')

# a=[1,2,3,4,5,6,7,8]
# print(*a)
# print(*a,sep='/')

# a=[[0]*4 for x in range(5)]
# print(*a,sep='/')

# a=[1,2,3,4]
# # print(a.pop())
# # print(a.pop(2))
# a.remove(3)
# print(a)

# a=[2,2,1,2,3,4,2]
# # a.insert(2,100)
# # print(a)
# # del a[1]
# # print(a)
# print(a.count(2))

# x={'a':ord('a'),'b':ord('b'),'A':ord('A'),'B':ord('B')}
# y=dict(a=ord('a'),b=ord('b'),A=ord('A'),B=ord('B'))
# print("x:",x)
# print("x:",x.keys())
# print("x:",x.values())
# print('y:',y)
# print('y:',y.items())
# # print('y:',y)
# print('a' in x.keys())

# a=[['a',1],['b',2]]
# dict_a=dict(a)
# # print(dict_a)
# b=['ab','cd']
# dict_b=dict(a)
# dict_a.get('a')
# dict_a['a']='b'
# print(dict_a.get('a'))
# c={**dict(a),**dict(b)}
# print(c)
# b=dict(a)
# print(del b['a'])
# print(b)
# a=('a','b','c','d','e')
# b={a[x]:x for x in range(len(a))}
# print(b)

# def my_range(first=0,last=5,step=2):
#     number=first
#     while number<last:
#         yield number
#         number+=step
# r=my_range(0,10,1)
# print(list(r))
# print(list(r))

# def gogo(*args):
#     print(args)
#     print(*args)
#
# a,b,c,d=map(int,input().split())
# gogo(a,b,c,d)

# x=(1,2,3)
# y=('a','b','c')
# for a,b in zip(x,y):
#     print(f'{a}:{b}')

##decorator
