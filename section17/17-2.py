#ans

"""
N: 10G
O: 15G
*をNかOに置き換えて置き換えた分だけ請求する
"""

print('なんでも回文にします。入力してください')
palindrome = input('入力:')
n_count = 0
o_count = 0
for idx, string in enumerate(palindrome):
    if palindrome[idx] == palindrome[-idx-1] == '*':
        x = palindrome.replace(string, 'N')
        print(x)
        n_count += 1
    elif palindrome[idx] == '*' and palindrome[-idx-1] == 'N':
        x = palindrome.replace(string, 'N')
        n_count += 1
        print(x)
    elif palindrome[idx] == '*' and palindrome[-idx-1] == 'O':
        x = palindrome.replace(string, 'O')
        print(x)
        o_count += 1
    
print(f'出力:{x}')
print(f'n:{n_count}, o:{o_count}')
print(f'{n_count*10+o_count*15}Gになります')