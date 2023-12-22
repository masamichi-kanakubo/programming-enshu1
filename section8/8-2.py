#ans

def synthesize(weapon1, weapon2):
    
    if weapon1 > weapon2:
        new_weapon = weapon1*1.2+weapon2*0.8
    else:
        new_weapon = weapon1*0.8+weapon2*1.2
    return new_weapon

print('金の剣と銀の剣の攻撃力を入力してください。')

try:
    offense1 = int(input('金の剣の攻撃力:'))
    offense2 = int(input('銀の剣の攻撃力:'))
except ValueError:
    print('無効な入力です。')
    exit()
    
print('勇者は金の剣と銀の剣を合成の箱にいれた。')

new_offense = int(synthesize(offense1, offense2))
print('合成の剣を手に入れた！')
print(f'合成の剣の攻撃力:{new_offense}')