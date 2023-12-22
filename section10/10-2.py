#ans

offenses = [32, 33, 21, 28, 36, 23, 25, 30]

print('勇者の守備力を入力してください。')
try:
    defense = int(input('勇者の守備力:'))
except ValueError:
    print('無効な入力です。')
    exit()
    
for idx in range(len(offenses)):
    print(f'スライム{idx+1}が現れた！') 

print('なんとスライムたちは合体して体当たりしてきた！')

sum = 0
for offense in range(len(offenses)):
    sum += offenses[offense]

damage = sum - defense
if damage > 0:
    print(f'勇者は{damage}のダメージを受けた！')
else:
    print('勇者はダメージを受け付けない！')