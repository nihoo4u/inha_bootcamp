# a=[['a','b'],['c','d']] # list->dict
# print(dict(a))
#
# b=['af','sd','df'] # str->dict
# print(dict(b))

# c={'a':"c",'b':'d'} #change,add
# c['a']='sdfsdf'
# c['c']='dfdfd'
# print(c)
#
# print(c.get('a'))


sugang=dict(subject='pytoon',db='kang',cpp='song')
# for subject,professor in sugang.items():
#     print(subject,professor)

for k in sugang:
    print(k, end=' ')
print()
for k in sugang.values():
    print(k, end=' ')
print()

for k in sugang.keys():
    print(k, end=' ')
print()
for k in sugang.items():
    print(k)