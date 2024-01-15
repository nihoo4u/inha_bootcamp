a=[1,2,3]
b=a
a[0]=100
print(b)


base_number=int(input('INput base number: '))
exponent_number=int(input('INput exponent number: '))
print(f'밑은 {base_number},"지수는 {exponent_number},결과값은 {base_number**exponent_number}')