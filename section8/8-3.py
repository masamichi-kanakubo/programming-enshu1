#ans

def fire(offense, defense):
    damage = offense -defense
    return damage


print('魔法使いの魔力とゴーレムのHP、魔法防御力を入力してください。')

try:
    offense = int(input('魔法使いの魔力:'))
    hp = int(input('ゴーレムのHP:'))
    defense = int(input('ゴーレムの魔法防御力:'))
except ValueError:
    print('無効な入力です。')
    exit()

judge = True
while judge:
    decision = input('[0]魔法/[1]にげる:')
    if decision == str(1):
        print('魔法使いはにげた。')
        break
    
    if decision != str(0):
        break
    
    print('魔法使いはファイアを唱えた！')
    damage = fire(offense, defense)
    if damage <= 0:
        print('ゴーレムはダメージを受け付けない！')
        continue

    print(f'ゴーレムに{damage}のダメージを与えた！')
    hp -= damage
    if hp > 0:
        print(f'ゴーレムのHP:{hp}')
    else:
        hp = 0
        print(f'ゴーレムのHP:{hp}')
        print('ゴーレムを倒した')
        judge = False


"""
ネストは見ずらくなるので極力使わずに書く
山にようなコードではなくフラットなフローで書く
"""