#ans

try:
    lv1 = int(input('勇者のレベル：'))
    lv2 = int(input('戦士のレベル：'))
    lv3 = int(input('魔法使いのレベル：'))
    lv4 = int(input('僧侶のレベル：'))
except ValueError:
    print('無効な入力です。')
    exit()

list = [lv1,lv2,lv3,lv4]

print(f'パーティの中で最もレベルの高いメンバのレベルは{max(list)}です。')

 