#ans
import random

def critical_strile():
    attack = random.randint(0,4)
    if attack == 0:
        print('かいしんのいちげき！')
        print('ドラゴンを倒した！')
    else:
        print('こうげきにっぱいした！')
        print('勇者たちは全滅した.....')
    return 


print('勇者たちの前にドラゴンが現れた！')

try:
    decision = int(input('[0]にげる/[1]攻撃:'))
except ValueError:
    print('無効な入力です。')
    exit()

if decision == 0:
    critical_strile()
elif decision == 1:
    print('逃げられない!')
    print('勇者たちは全滅した.....')
else:
    print('無効な入力です。')
