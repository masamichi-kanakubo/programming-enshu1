#ans

print('勇者の攻撃欲とガーゴイルのHP、守備力を入力してください。')

try:
    offense = int(input('勇者の攻撃力:'))
    hp = int(input('ガーゴイルのHP:'))
    defense = int(input('ガーゴイルの守備力:'))
except ValueError:
    print('無効な入力です。')
    exit()

flag = True
while flag:
    print('ガーゴイルに{}のダメージを与えた！'.format(offense-defense))
    if hp - (offense - defense)  > 0:
        #不等号の評価
        print('ガーゴイルのHP:{}'.format(hp-(offense - defense)))
        hp -= offense - defense
    else:
        flag = False
    #whileループの終了条件
        

print('ガーゴイルをたおした！')
        