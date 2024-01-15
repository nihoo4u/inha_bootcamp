num1=int(input("input the number"))
num2=int(input("input the number"))
# q=num1//num2
# r=num1%num2

# print(f'몫은 {q}이고 나머지는 {r}입니다')
print(f'몫은 {divmod(num1,num2)[0]}이고 나머지는 {divmod(num1,num2)[1]}입니다')
