#ans

def blizzard(defenses, offense):
    for index in range(1, len(defenses)+1, 1):
        #forループ内でのindexとリスト内のインデックスが別物で一つずれているのでindexを１ひいて修正
        if offense - defenses[index-1] >= 0:
            print('コカトリス{}に{}のダメージを与えた！'.format(index, offense-defenses[index-1]))
        else:
            print('コカトリス{}はダメージを受け付けない!'.format(index))

defenses = [38, 42, 22, 120, 27]

print('魔法使いの魔力を入力してください。')

try:
    offense = int(input('魔法使いの魔力:'))
except ValueError:
    print('無効な入力です。')
    exit()

for index in range(1, len(defenses)+1, 1):
    print('コカトリス{}が現れた！'.format(index))

print('魔法使いはブリザードを唱えた！')
blizzard(defenses, offense)