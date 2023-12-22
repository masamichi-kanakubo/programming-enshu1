#ans

import random

number = 1
while number <= 30:
    if number % 3 == 0 and number % 5 == 0:
        expected = 'FizzBuzz'
        if random.randint(1, 4) == 1:
            expected = str(number)
            print(f'女主人:{expected}')
            print('勇者は勝負に勝った')
            break
    elif number % 3 == 0:
        expected = 'Fizz'
        if random.randint(1, 4) == 1:
            expected = str(number)
            print(f'女主人:{expected}')
            print('勇者は勝負に勝った')
            break
    elif number % 5 == 0:
        expected = 'Buzz'
        if random.randint(1, 4) == 1:
            expected = str(number)
            print(f'女主人:{expected}')
            print('勇者は勝負に勝った')
            break
    else:
        expected = str(number)
    
    print(f'女主人:{expected}')
    number += 1
    
    hero = input('勇者:')
    if number % 3 == 0 and number % 5 == 0:
        if hero != 'FizzBuzz':
            print('勇者は間違えた！')
            print('勇者は酒場からたたき出された！')
            break
    elif number % 3 == 0:
        if hero != 'Fizz':
            print('勇者は間違えた！')
            print('勇者は酒場からたたき出された！')
            break
    elif number % 5 == 0:
        if hero != 'Buzz':
            print('勇者は間違えた！')
            print('勇者は酒場からたたき出された！')
            break
    else:
        if hero != str(number):
            print('勇者は間違えた！')
            print('勇者は酒場からたたき出された！')
            break
    
    number += 1
if number >= 30:
    print('勇者は勝負に勝った')
