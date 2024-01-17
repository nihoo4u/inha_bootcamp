import copy

subjects=["a","b","c"]
a=subjects
b=subjects.copy()
c=list(subjects)
d=subjects[:]
e=copy.deepcopy(a)
print(subjects,a,b,c,d)
subjects[1]="x"
print(subjects,a,b,c,d)