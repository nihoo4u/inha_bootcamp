letter=input('input the spelling')
# vowels={'a','e','i','o','u'}
vowels='aeiou'
if letter in vowels:
    print(f'{letter}is  included')
else:
    print(f'{letter}is not included')