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


print("名前:{}".format(golem.name))
print("HP:{}".format(golem.hp))
print("攻撃力:{}".format(golem.offense))
print("守備力:{}".format(golem.defense))