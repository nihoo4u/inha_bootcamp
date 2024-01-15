menu=int(input("1)f->c 2>c->f 3)quit"))
if menu==1:
    f=float(input('input f'))
    print(f'f:{f} and c:{(f-32)*5/9:.3f}')
elif menu==2:
    c=float(input('input c'))
    print(f'c:{c} and f:{c*9/5+32}')
