#ans

defenses = [38, 42, 22, 120, 27]

print('魔法使いの魔力を入力してください。')
try:
    offense = int(input('魔法使いの魔力:'))
except ValueError:
    print('無効な入力です。')
    exit()

for idx in range(1, len(defenses)+1, 1):
    print(f'コカトリス{idx}が現れた！')

print('魔法使いはブリザードを唱えた！')

for idx in range(len(defenses)):
    damage = offense - defenses[idx]
    if damage <= 0:
        print(f'コカトリス{idx+1}はダメージを受け付けない！')
    else:
        print(f'コカトリス{idx+1}に{damage}のダメージ！')
        