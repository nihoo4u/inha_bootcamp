#8.1
e2f={'dog':'chien','cat':'cha','walrus':'mores'}
#8.2
print(e2f['walrus'])
#8.3
f2e=dict()
for a,b in e2f.items():
    f2e[b]=a
print(f2e)
#8.4
print(e2f['dog'])
#8.5
print(*e2f.keys(),end=' ')
#8.6