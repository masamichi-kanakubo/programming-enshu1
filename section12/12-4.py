#ans

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def move(self, x, y):
        self.x = x
        self.y = y


class Character(Point):
    def __init__(self, name, x_0, y_0):
        super().__init__(x_0, y_0)
        self.name = name
        

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
