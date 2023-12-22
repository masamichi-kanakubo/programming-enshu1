#ans

print('そなた 名は何と申す？')
name = input('名前を入力してください:')

if 'は' in name:
    replaced_name = name.replace('は', 'ひゃ')
    
print('{}と申すのか 良い名じゃな'.format(replaced_name))