#ans

print('勇者の攻撃力とオークの守備力を入力してください')

try:
    attack = int(input('勇者の攻撃力：'))
    defence = int(input('オークの守備力：'))
    times = int(input('何回攻撃しますか？：'))
except ValueError:
    print('無効な入力です。')
    exit()
    
print('勇者はオークに疾風の如く斬りかかった！')

judge = attack - defence
if judge > 0 :
    for time in range(1, times+1):
        print('勇者の攻撃！('+str(time)+'回目)')
    damage = 20*times
    print(str(times)+'回の攻撃でオークに総合で'+str(damage)+'のダメージを与えた！')   
else:
    print('オークはダメージを受け付けない！') 
    

"""
judgeの変数に攻撃が当たるか判定するための数値をもたせておく
if文でjudgeを判定してpass(０以上)ならそれ以下のforループのフローを実行
"""