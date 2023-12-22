#ans

"""
save11.txt
save12.txt
save13.txt
"""

try:
    answer = int(input('ゲームを再開しますか？はい->1, いいえ->0:'))
except ValueError:
    print('無効な値です。')
    exit()

if answer == 1:
    select_file = input('再開するファイルを選んでください:')
    with open(f'{select_file}', 'r', encoding='utf-8') as file:
        print(file.read()+'からゲームを再開します。')
else:
    print('ゲームの再開をキャンセルしました。')