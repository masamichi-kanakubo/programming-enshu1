# Section5

## 5-1
damageなどで演算をif文に入れずに変数としていっかつで扱う
できるだけ一つの式の中にある変数は減らす, コードを短くする

## 5-2
コード内でのmax関数の仕組みとしては、
```py
if lv1 >= lv2 and lv1 >= lv3 and lv1 >= lv4:
    max = lv1
elif lv2 >= lv1 and lv2 >= lv3 and lv2 >= lv4:
    max = lv2
elif lv3 >= lv1 and lv3 >= lv2 and lv3 >= lv4:
    max = lv3
elif lv4 >= lv1 and lv4 >= lv2 and lv4 >= lv3:
    max = lv4

print(f'パーティの中で最もレベルの高いメンバのレベルは{max}です。')
```
と同意味。どちらで解答しても処理が実行される。

## 5-3
ifなどの条件を設定する場合、その条件が明示的であるようにコードを書くと良い。

## 5-4
選択しがながったるいので改行\nを使う
わざわざ改行を行っているので選択しの横に入力部分を作るのは野暮
改行して選択用の行を作る
answerをstringでうけとるので例外処理は不要
