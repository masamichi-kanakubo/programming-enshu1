#ans

class Monster:
    def name(self, name):
        self.name = name
    
    def hp(self, hp):
        self.hp = hp
    
    def offense(self, offense):
        self.attack = offense
    
    def defense(self, defense):
        self.defence = defense

golem = Monster()
golem.name = "ゴーレム"
golem.hp = 256
golem.offense = 123
golem.defense = 111

dragon = Monster()
dragon.name = "ドラゴン"
dragon.hp = 489
dragon.offense = 131
dragon.defense = 99

slime = Monster()
slime.name = "スライム"
slime.hp = 12
slime.offense = 11
slime.defense = 9

monsters = []

monsters.append(golem)
monsters.append(dragon)
monsters.append(slime)

for idx in range(len(monsters)):
    print('{}\t{}\t{}\t{}'.format(monsters[idx].name, monsters[idx].hp, monsters[idx].offense, monsters[idx].defense))

