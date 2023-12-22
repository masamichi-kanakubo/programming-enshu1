#ans

items = {}

with open('item.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()
    
for line in lines:
    parts = line.strip().split(',')
    if len(parts) == 2:
        name, value = parts[0], int(parts[1])
        items[name] = value

        
with open('sold.txt', 'w', encoding='utf-8') as file:
    for item in items:
        if items[item] > 10:
            sum = 0
            while items[item] > 10:
                items[item] -= 1
                sum += 1
            print(f'{item}を{sum}個売り払った')
            file.write(f'{item}を{sum}個売り払った\n')
        elif 5 < items[item] <= 10:
            sum = 0
            while items[item] > 5:
                items[item] -= 1
                sum += 1
            print(f'{item}を{sum}個売り払った')
            file.write(f'{item}を{sum}個売り払った\n')
  
          
"""
最適解がパッと思いつかなかったのでネストでごり押しする形になってしまった
のちのち変更すると思う
ChatGPTに同じ処理でネストを使わないようなコードフローを提案させたところ
処理の意味自体をはき違えて返ってきたのであきらめた
動いているのでとりあえずpushしておく
追記
ランタイムがn回のforループで終わるので仕方ないからこれでcommitする
"""