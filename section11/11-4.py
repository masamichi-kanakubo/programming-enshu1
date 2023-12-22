#ans

def swap(party1, party2):
    flag = 0
    
    for name, hp in party2.items():
        name2 = name
        hp2 = hp
    for name, hp in party1.items():
        name1 = name
        hp1 = hp
        if hp1 >= hp2:
            party1[name1] = hp2
            flag = 1
        
    
    return flag

party1 = {'勇者':32, '魔法使い':14, '僧侶':22}
party2 = {'ゴースト':15}

for name, hp in party1.items():
    print(f'{name}のHP:{hp}')
    
for name, hp in party2.items():
    print(f'{name}のHP:{hp}')
    
print('ゴーストが現れた！')
print('ゴーストはスワップを唱えた！')

flag = swap(party1, party2)
if(flag == 0):
    print('何もおこらなかった！')
if(flag == 1):
    print('勇者たちのHPが入れ替わってしまった!')
    for name, hp in party1.items():
        print(f'{name}のHP:{hp}')


"""
itemsメソッドは辞書のキーと値をタプルにしてリストにして返す関数
それを決め打ちしたdictから値を取り出して値を比較する関数を定義
値の変更が行われたかflagで判定
"""