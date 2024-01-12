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
