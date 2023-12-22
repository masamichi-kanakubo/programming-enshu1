# ans

print('勇者はエンカウントしたモンスターを見てみた。')
monsters = {}

with open('encount.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()
    
for line in lines:
    parts = line.strip().split()
    if len(parts) == 2:
        name, value = parts[0], int(parts[1])  
        monsters[name] = value  

for name, counts in monsters.items():
    print('{}:{}'.format(name, counts))
    
maxcounts = 0
maxname = ''

for name, counts in monsters.items():
    if int(maxcounts) < int(counts):
        maxcounts = counts
        maxname = name

print('最もエンカウント数が多いのは{}で{}回だった！'.format(maxname, maxcounts))