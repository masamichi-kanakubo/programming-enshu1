# ans

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
    