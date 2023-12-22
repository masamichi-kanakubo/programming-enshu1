# ans

"""
先に問題の情報を整理する
S: 相手よりレベル３以上
A: 相手よりレベルが高くレベル差は３未満
B: 相手とレベルが同じorレベル差が-1
C: 相手よりレベルが２以上下
表を完成させることからおそらくi*jのループを考える
実行例をみるかぎりS,A,B,Cを表の値として入れていけばよさそう
一行ずつforを繰り返すように実行
my_lvをforループで回すとレベル10で少しずれるのでif文で修正
"""

print(" 　　|Lv 1 Lv 2 Lv 3 Lv 4 Lv 5 Lv 6 Lv 7 Lv 8 Lv 9 Lv 10")
print("-----+-----------------------------------------------------------")

for my_lv in range(1, 11):
    lv_table = []

    for enemy_lv in range(1, 11):
        judge = my_lv - enemy_lv
        if judge >= 3:
            rank = "S"
        elif 0 < judge < 3:
            rank = "A"
        elif judge == 0 or judge == -1:
            rank = "B"
        else:
            rank = "C"

        lv_table.append(rank)
    
    #ズレ対策
    if my_lv == 10:
        print(f"Lv{my_lv} |", end=" ")
    else:    
        print(f"Lv{my_lv}  |", end=" ")
    for rank in lv_table:
        print(rank, end="    ")
    print()  #改行
    