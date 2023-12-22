#ans

note = 'liesandtruth'

print('合言葉はこの中に隠されている')
print('「{}」'.format(note))

print('汝 真の勇者であることを示せ')
str1 = input('合言葉は（ヒント：８文字目から）:')

if note[7:] == str1:
    print('扉の中へ入るがよい！')
else:
    print('すぐにここから立ち去られよ！')