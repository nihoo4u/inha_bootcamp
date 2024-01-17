# import copy
# subject=[1,2,3]
# a=subject
# b=subject[:]
# c=subject.copy()
# d=copy.deepcopy(subject)
# print(subject,a,b,c,d)
# print(id(subject),id(a),id(b),id(c),id(d))
# subject[0]=100
# print(subject,a,b,c,d)
# print(id(subject),id(a),id(b),id(c),id(d))


import copy
subject=2
a=subject

d=copy.deepcopy(subject)
print(subject,a,d)
print(id(subject),id(a),id(d))
subject=3
print(subject,a,d)
print(id(subject),id(a),id(d))


