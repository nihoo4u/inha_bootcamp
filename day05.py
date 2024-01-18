def whatis(thing):
    if thing is None:
        print(thing,"is None")
    elif thing:
        print(thing,"is true")
    else:
        print(thing,"is false")
whatis(' ')