#ans

items = {}

with open('item.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()
    
for line in lines:
    parts = line.strip().split(',')
    if len(parts) == 2:
        name, value = parts[0], int(parts[1])
        items[name] = value

        
with open('sold.txt', 'w', encoding='utf-8') as file:
    for item in items:
        if items[item] > 10:
            sum = 0
            while items[item] > 10:
                items[item] -= 1
                sum += 1
            print(f'{item}を{sum}個売り払った')
            file.write(f'{item}を{sum}個売り払った\n')
        elif 5 < items[item] <= 10:
            sum = 0
            while items[item] > 5:
                items[item] -= 1
                sum += 1
            print(f'{item}を{sum}個売り払った')
            file.write(f'{item}を{sum}個売り払った\n')
  
          
