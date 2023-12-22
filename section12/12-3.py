#ans

class Character:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y
        
    def move(self, x, y):
        self.x = x
        self.y = y
        

player = Character('勇者', 5, 5)
monster = Character('オーガ', 6, 6)

while True:
    print('勇者の現在位置は({}, {})です。'.format(player.x, player.y))
    try:
        direction = int(input('どの方向に移動しますか？(8->北, 6->東, 4->南, 2->西, 0->終了:)'))
    except ValueError:
        print('無効な値です。')
        continue
    if direction == 8:
        player.move(player.x, player.y - 1)
    elif direction == 6:
        player.move(player.x + 1, player.y)
    elif direction == 4:
        player.move(player.x, player.y + 1)
    elif direction == 2:
        player.move(player.x - 1, player.y)
    elif direction == 0:
        break
    else:
        print('選択しの中から選んでください。')
        continue
    
    if player.x == monster.x and player.y == monster.y:
        print('オーガが現れた！')
        break
    
"""
move()メソッド内のx, yがかぶっているので
パラメータをdx, dyなどに変更するほうがコードとしては無難
__init__でつかった先に使ってしまったのでなるべく同じ名前は避けたい
"""