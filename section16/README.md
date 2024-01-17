# Section16

## 16-1
Pythonの文字列変換の基礎的な問題。シーザー暗号のロジックは与えられた暗号鍵をアルファベットを正則的に別のアルファベットに変換する。
以下のコードでロジックを理解したい。

```py
string = 'abcdefghijklmnopqrstuvwxyz .,-'

plaintext = ''
for char in ciphertext:
        
    idx = string.find(char)

    decrypted_idx = (idx - shift) % len(string)
    if decrypted_idx < 0:
        decrypted_idx += len(string) 
    elif decrypted_idx > len(string):
        decrypted_idx -= len(string)
        
    decrypted_char = string[decrypted_idx]
    plaintext += decrypted_char 
```
文字を一つ一つ変換するという発想から`for`ループを使用することをまず思いつく。ここで`char`と`idx`を分けて考えているが`enumerate`で同時に取得する方法も考えられるが、`char`が同じアルファベットであった場合、それらを識別する`idx`でエラーが起きなくてもデバックで欲しい値を取って来れない可能性が高い。

ロジック部分はシンプルな処理で通す。取得した`idx`と自分がずらしたい分の`shift`の差分を与えられた(アルファベット＋特殊文字)で割り、０以下即ちAより前になった場合、-に戻るようにしたいので逆に-からどのくらい離れているかという発想で`decrypted_idex`は考える。また文字列が-をこえる場合その逆を考えれば良い。

## 16-2
基礎的な`while`ループの問題。次の処理がかけていればOK
```py
mistake = 0
while mistake < 5:
    print('わしが思い浮かべた数を当ててみよ。')
    try:
        answer = int(input('いくつだと思う:'))
    except ValueError:
        print('無効な入力です。')
        exit()
    if answer == value:
        print('正解じゃ。通るが良い')
        break
    elif answer < value:
        print('もっと大きいわい')
        mistake += 1
    else:
        print('もっと少ないわい')
        mistake += 1
```
`mistake`はwhileループでお馴染みのフラグである。whileの基本的な考え方はこのフラグがTrueになる条件で中の処理を書いていくことである。おそらく想定している間違いであるwhileの外でinput関数を使ってしまうことを避けたい。

## 16-3

