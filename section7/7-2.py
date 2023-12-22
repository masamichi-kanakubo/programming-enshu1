#ans

print('勇者の攻撃力とガーゴイルのHP、守備力を入力してください。')

try:
    attack = int(input('勇者の攻撃力:'))
    hp = int(input('ガーゴイルのHP:'))
    defense = int(input('ガーゴイルの防御力:'))
except ValueError:
    print('無効な入力です。')
    exit()
    
damage = attack - defense
if damage > 0:
    while hp > 0:
        print(f'ガーゴイルに{damage}のダメージを与えた！')
        hp -= damage
        if hp <= 0:
            hp = 0
        print(f'ガーゴイルのHPは{hp}になった！')
        print('ガーゴイルをたおした！')