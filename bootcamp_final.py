b=[]
for i in range(1,6):
    b.append(i**2)
print(b)



a=[x**2 for x in range(1,6)]
print(a)

a=[x for x in range(1,10) if x%2==1]
print(a)

a=["a","b","c"]
b=[1,2,3]
for x,y in zip(a,b):
    print(f'{x} is {y}th memory')

rows=range(1,4)
cols=range(1,3)
for row in rows:
    for col in cols:
        print((row,col))


cells=[(rol,col) for rol in rows for col in cols]
print(cells)

for a,b in cells: #unpacking
    print(a,b)

