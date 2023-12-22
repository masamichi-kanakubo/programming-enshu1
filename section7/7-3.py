#ans

print('勇者の攻撃力とゴーレムのHP、守備力を入力してください。')

try:
    offense = int(input('勇者の攻撃力:'))
    hp = int(input('ゴーレムのHP:'))
    defense = int(input('ゴーレムの防御力:'))
except ValueError:
    print('無効な入力です。')
    exit()

decision = True
while decision:
    try:
        option = int(input('[0]たたかう/[1]にげる:'))
    except ValueError:
        print('無効な入力です。')
        continue
    if option == 1:
        print('勇者はにげだした！')
        decision = False
        continue
    
    damage = offense - defense
    if damage > 0:
        print(f'ゴーレムに{damage}のダメージを与えた！')
    else:
        print('ゴーレムはダメージをうけていない！')
        continue
    
    hp -= damage
    if hp <= 0:
        hp = 0
        print('ゴーレムをたおした！')
        decision = False
    else:
        print(f'ゴーレムのHP:{hp}')


"""
入力に関する例外処理の実行を補足している
intで受けているので文字が入ったときはValueErrorを返す
optionでは1がかえったときにFalseで処理を終わらせる
"""
