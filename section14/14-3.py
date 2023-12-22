#ans

def delnum(str1):
    #絶対forループで回したほうがいい
    for char in str1:
        if char == "0":
            print("", end="")
        elif char == "1":
            print("", end="")
        elif char == "2":
            print("", end="")
        elif char == "3":
            print("", end="")
        elif char == "4":
            print("", end="")
        elif char == "5":
            print("", end="")
        elif char == "6":
            print("", end="")
        elif char == "7":
            print("", end="")
        elif char == "8":
            print("", end="")
        elif char == "9":
            print("", end="")
        else:
            print(char, end="")
            
print("")

str1 = "T2s3u6ki9 n3o4 h9i8ka5ri ni3 4t1er3a7sa8re7ru to02ki m18ic2hi1 h5ah6i9rak0a9r02en."

print('石板に何やら文字が書かれている')
print(str1)

print('デルナムを唱えた！')
print('何と石板から数字が取り除かれていく')

delnum(str1)