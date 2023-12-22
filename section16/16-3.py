#ans

import random

def get_random_int():
    while True:
        #0はふくまないのであらかじめ検索範囲を小さくしておく
        number = random.randint(1111, 9999)  
        digits = [int(digit) for digit in str(number)]
        if 0 not in digits and len(set(digits)) == 4:
            return number

random_int = get_random_int()
print(random_int)

print('私の思い浮かべた数字を当てることができたら、次に進むべき道を示しましょう。')


mistake = 0
while mistake < 5:
    try:
        answer = int(input('いくつだと思いますか:'))
    except ValueError:
        print('無効な入力です。')
        exit()
    
    hit = 0
    blow = 0
    
    for idx in range(len(str(random_int))):
        if str(answer)[idx] == str(random_int)[idx]:
            hit += 1
        elif str(answer)[idx] in str(random_int):
            blow += 1
        
    if hit == 4:
        print('正解です。次に進むべき道はあちらです。')
    else:
        print(f'ヒット数は{hit}、ブロー数は{blow}です。')
        mistake += 1

if mistake >= 5:
    print('あなたはまだここを通る資格はないようです。')
    print('勇者たちは洞窟の入り口まで戻された。。。')        