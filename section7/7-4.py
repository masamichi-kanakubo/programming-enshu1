#ans

print('勇者の最大HPと現在のHPを入力してください。')

try:
    max_hp = int(input('勇者の最大HP:'))
    hp = int(input('現在のHP:'))
except ValueError:
    print('無効な入力です。')
    exit()

recovery_magic = 10
    
recovery = True
while recovery:
    print('僧侶はホイミを唱えた')
    hp += recovery_magic
    if hp >= max_hp:
        hp = max_hp
        recovery = False
    print(f'勇者のHPが{hp}になった')