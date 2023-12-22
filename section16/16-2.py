#ans

import random

value = random.randrange(0, 1000)
#print(value)

mistake = 0
while mistake < 5:
    print('わしが思い浮かべた数を当ててみよ。')
    try:
        answer = int(input('いくつだと思う:'))
    except ValueError:
        print('無効な入力です。')
        exit()
    if answer == value:
        print('正解じゃ。通るが良い')
        break
    elif answer < value:
        print('もっと大きいわい')
        mistake += 1
    else:
        print('もっと少ないわい')
        mistake += 1

if mistake >= 5:
    print('愚か者め！ここは通さぬ！')
    print('勇者はドラゴンに通された。。。')