#ans

print('勇者たちはウッドパルナの村についた。')
try:
    answer = int(input('ゲームをセーブしますか。はい->1, いいえ->0:'))
except ValueError:
    print('無効な値です。')
    exit()

if answer == 1:
    select_file = input('ゲームをセーブするフィルを選んでください:')
    with open(f'{select_file}', 'w', encoding='utf-8') as file:
        file.write('ウッドパルナの村についた。\n')
        print('セーブしました。')
else:
    print('勇者たちは次の村へ向かった。')