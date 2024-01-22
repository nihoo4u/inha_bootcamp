# ##direct access
# class Pockemon:
#     def __init__(self,name):
#         self.name=name
#     def getter(self):
#         return self.name
# class Pika(Pockemon):
#     pass
# #__init__이용해 직접 할당하는 방법 (direct access)
# direct_access=Pockemon('Pika')
# print(direct_access.name)
# print(direct_access.getter())
#
# ##direct_access 객체의 속성이 direct한 방법,getter을 이용해서 name을 불러모으고 있다
# direct_access.name='2'
# print(direct_access.getter())
#
#
#
# # getter,setter,method1_using property
# class Duck:
#     def __init__(self,input_name):
#         self.__hiddenname=input_name
#     def get_name(self):
#         print(f"get name which is {self.__hiddenname}")
#         return self.__hiddenname
#     def set_name(self,input_name):
#         print(f"set name from {self.__hiddenname} to {input_name}")
#         self.__hiddenname=input_name
#     # name=property(get_name,set_name) #property가 함수이므로 객체.name으로 불러올 수 있다
#
# class Duckbaby(Duck):
#     pass
#
#
# before using property
# print(a.name)
# print(a.get_name())
# a.set_name('PNY')
# print(a.get_name())
# print(a.name)
#
# #after using property
# print(a.name)
# a.name='43543'
# print(a.name)
#
#
# # getter,setter,method2_using property
# #원래부터 속성 또한 잘 가져와쓸 수 있었지만 property와 name.setter을 통해 a.name=2 이런 식이 가능해졌다
class Duck:
    def __init__(self,input_name):
        self.hiddenname=input_name
    @property #property를 getter 위에
    def name(self):
        print(f"get name which is {self.hiddenname}")
        return self.hiddenname
    @name.setter #getter이름.setter
    def name(self,input_name):
        print(f"set name from {self.hiddenname} to {input_name}")
        self.hiddenname=input_name


class Duckbaby(Duck):
    pass

a=Duck('PJY')
print(a.name)
a.name='Keung'
print(a.name)
#
# # calculatign property
# class Circle:
#     def __init__(self,radius):
#         self.radius=radius
#     @property
#     def diameter(self):
#         return 2*self.radius
# a=Circle(6)
# print(a.radius)
# # print(a.diameter())
# print(a.diameter)
#
#
#
# #a.b b에 메서드뿐만 아니라 속성도 올 수 있다.
# class Wonder:
#     def __init__(self,x):
#         self.variable=x
#     def findit(self,x):
#         return x**2
#     num=1
# a=Wonder(3)
# print(a.num)
# print(a.findit(3))
# print(a.variable)
#
#
#
# name mangling #바로 위 소스코드처럼 속성에 대해서도 찾을 수가 있는데 언더바 두번 넣으면 바로 찾을 수 없
# class Duck:
#     def __init__(self,input_name):
#         self.__hiddenname=input_name
#     @property #property를 getter 위에
#     def name(self):
#         print(f"get name which is {self.__hiddenname}")
#         return self.__hiddenname
#     @name.setter #getter이름.setter
#     def name(self,input_name):
#         print(f"set name from {self.__hiddenname} to {input_name}")
#         self.__hiddenname=input_name
#
#
#
# class Duckbaby(Duck):
#     pass
#
# a=Duck('PJY')
# print(a.name)
# a.name='Keung'
# print(a.name)
# print(a.k)
#
#
#
#
#
#
#

import random
a=[1,2,3,4]
position=random.randint(3,10)
try:
    print(a[position])
except IndexError as err:
    print(f"input the number not over {len(a)} {err}")
except ValueError:
    print("input the integer number",err)
except Exception as err:
    print(f"I can't manange you ",err)



