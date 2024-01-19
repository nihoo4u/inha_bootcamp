# a=[1,2,3,4]
# print(a)
# print(id(a))
# def change_it():
#     a[0]=2
#     print(a)
#     print(id(a))
#
#
# change_it()
# print(a)
# print(id(a))

# a=2
# print(a)
# print(id(a))
# def change_it():
#     a=3
#     print(a)
#     print(id(a))
#
#
# change_it()
# print(a)
# print(id(a))
# b=3
# print(b)
# print(id(b))
# def change_int():
#     global b
#     b=2
#     print(id(b))
#
# change_int()
# print(b)


# def test(f): #decorator
#     def func(*args,**kwargs):
#         print('start')
#         f(2)
#         print('end')
#     return func
#
# @test
# def gogo(x):
#     for i in range(x):
#         print(i)

# start_func=test(gogo)
# start_func()

# gogo()



# def iam():
#     print(2)
#
# print(iam.__name__)

#
# short_list=[1,2,3]
# position=5
# try:
#     print(short_list[position])
# except:
#     print('it is hard to go..')


###
# import random
# numbers=[random.randint(1,5)]
# class OopsException(Exception):
#     pass
#
# try:
#     pick = int(input())
#     print(numbers[pick])

# class Pockemon():
#     # pass
#     def __init__(self,name,):
#         self.name=name
#         print(f" add {name} pocketmon")
#     def attack(self,target):
#         print(f'{self.name}이 {target.name}을 공격')
# charizard=Pockemon('lizamong')
# pikachu=Pockemon('pikachu')
# squirtle=Pockemon('squirtle')
# charizard.attack(squirtle)

# class Pokemon:
#     def __init__(self,name):
#         self.name=name
# class Pikachu(Pokemon):
#     pass
#
# p1=Pikachu('피카츄')
# print(p1.name)
# print(issubclass(Pikachu,Pokemon))



# class Animal:
#     def says(self):
#         return
# class Hores(Animal):
#     def says(self):

###질
# class Cat:
#     def __init__(self,name):
#         self.name=name
#     def surname(self,surname):
        # self.surname=surname

# a_cat=Cat('go')
# print(a_cat.name)
# print(a_cat.surname('df'))

# class FlyingMixin:
#     def fly(self):
#         return f"{self.name} is flying"
# class SwimmingMixin:
#     def swim(self):
#         return f"{self.name} is swimming"
#
#
# class Pokemon:
#     def __init__(self,input_name):
#         self.hidden_name=input_name
#     def attack(self):
#         return "공격"
#     def get_name(self):
#         print('inside getter')
#         return self.hidden_name
#
#     def set_name(self,input_name):
#         print('inside setter')
#         self.hidden_name=input_name
#
#     name = property(get_name, set_name)
#
# class Charizard(Pokemon,FlyingMixin):
#     pass
# class Gayarados(Pokemon,SwimmingMixin):
#     pass
#
# g1=Gayarados('Gayrados')
# c1=Charizard('Charizard')



