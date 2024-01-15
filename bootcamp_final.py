while True:
    menu=int(input("Input the number"))
    if menu==1:
        f=float(input('input f'))
        print(f'f:{f} and c:{(f-32)*5/9:.3f}')
    elif menu==2:
        c=float(input('input c'))
        print(f'c:{c} and f:{c*9/5+32}')
    else:
        print('terminate program')
        break
