#ans

def heal(hps):
    for i in range(len(hps)):
        hps[i] += 80
    return hps

hps = [32, 14, 22, 6]

for idx in range(len(hps)):
    print(f'プレイヤー{idx+1}のHP:{hps[idx]}')
    
print('僧侶はヒールを唱えた！')
heal(hps)

for idx in range(len(hps)):
    print(f'プレイヤー{idx+1}のHP:{hps[idx]}')


"""
forループでプレイヤーのHPを表示するところは
二回同じことをしているので関数にしたほうがよい
def parameter(hps):
    for idx in range(len(hps)):
        print(f'プレイヤー{idx+1}のHP:{hps[idx]}')
    return hps
    
parameter(hps)
"""