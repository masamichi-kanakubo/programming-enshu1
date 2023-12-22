#ans

print('勇者の攻撃力とスライムの防御力を入力してください。')
try:
    attack = int(input('勇者の攻撃力：'))
    defense = int(input('スライムの防御力：'))
except ValueError:
    print('無効な入力です。')
    exit()
    
damage = attack - defense
if damage <= 0:
    print('スライムはダメージを受け付けない。')
else:
    print(f'勇者はスライムに{damage}のダメージを与えた！')
    
"""
damageなどで演算をif文に入れずに変数としていっかつで扱う
できるだけ一つの式の中にある変数は減らす, コードを短くする
"""