#ans

str1 = "T2s3u6ki9 n3o4 h9i8ka5ri ni3 4t1er3a7sa8re7ru to02ki m18ic2hi1 h5ah6i9rak0a9r02en."

print('石板に何やら文字が書かれている。')
print(str1)

print('デルナムを唱えた！')
print('なんと石板から数字が取り除かれていく！')

for char in str1:
    if char.isdigit():
        str1 = str1.replace(char, '')
        
print(str1)