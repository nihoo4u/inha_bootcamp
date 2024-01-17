import random
drink_food={'위스키':'초콜릿','와인':'치즈','소주':'삼겹살','고량주':'왕꼬치'}

del drink_food['위스키']

print(drink_food)
drink_food_keys=list(drink_food)
print(drink_food.pop('와인'))
print(drink_food)

while True:
    menu=input(f'다음 술 중에 고르시오\n 1){drink_food_keys[0]},2){drink_food_keys[1]},3){drink_food_keys[2]},4){drink_food_keys[3]}')
    random_drink=random.choice(drink_food_keys)
    if menu=='1':
        print(f'{drink_food_keys[0]}에 어울리는 안주는 {drink_food[drink_food_keys[0]]}입니다')
    elif menu=='2':
        print(f'{drink_food_keys[1]}에 어울리는 안주는 {drink_food[drink_food_keys[1]]}입니다')
    elif menu=='3':
        print(f'{drink_food_keys[2]}에 어울리는 안주는 {drink_food[drink_food_keys[2]]}입니다')
    elif menu=='4':
        print(f'{drink_food_keys[3]}에 어울리는 안주는 {drink_food[drink_food_keys[3]]}입니다')
    else:
        print(f'{random_drink}에 어울리는 안주는 없습니다')




# print(drink_food_keys)
# print(drink_food_keys[0])

# cells={'a':'abc','b':'bcd','c':'cde','d':'def'}
# print(list(cells.keys()))

# first={'a':'agony','b':'bliss'}



