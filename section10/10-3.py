# ans

map = [
0, 0, 0, 0, 0, 0, 0,
0, 1, 2, 0, 0, 0, 0,
0, 2, 0, 0, 0, 0, 2,
0, 0, 0, 0, 0, 2, 1,
0, 0, 0, 0, 0, 0, 2,
0, 0, 2, 1, 2, 0, 0,
0, 0, 0, 0, 2, 0, 0,
0, 0, 0, 0, 2, 0, 0,
0, 0, 0, 0, 1, 2, 0,
]

print("-----------")
for i in range(len(map)):
    if map[i] == 0:
        print("  ", end="")
    elif map[i] == 1:
        print(" *", end="")
    else:
        print(" x", end="")
    if i % 7 == 0:
        print('')
print('')
print("-----------")

print("どこを調べますか？")

try:
    x = int(input("横の座標（０から６まで）:"))
    y = int(input("縦の座標（０から８まで）:"))
except ValueError:
    print("無効な入力です。")
    exit()

print(f'勇者は({x}, {y})を調べた。')

place = map[y * 7 + x]
if place == 0:
    print("しかしなにも見つからなかった。")
elif place == 1:
    print('なんと小さな宝石を見つけた！')
else:
    print('グールが現れた！')