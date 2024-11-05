class Character:
    def __init__(self, name, damage, health):
        self.name = name
        self.damage = damage
        self._health = health
        self.__skill = "ini adalah skill"
        self.__skill2 = "ini adalah skill 2"

    def status(self):
        return f"Name: {self.name}, Health: {self._health}, Damage: {self.damage}"
    
    def getskill(self):
        return self.__skill
    
    def setskill(self, new_skill):
        self.__skill = new_skill

    def getskill2(self):
        return self.__skill2
    
    def setskill2(self, new_skill2):
        self.__skill2 = new_skill2

    def gethealth(self):
        return self._health
    
    def sethealth(self, new_health):
        self._health = new_health

class Battle(Character):
    def __init__(self, name, damage, health):
        super().__init__(name, damage, health)
        print(self.status())
        print(f"Kesehatan diatur menjadi: {self.gethealth()}")
        
    def transformskill(self):
        health = self.gethealth()
        if health >= 50:
            self.setskill("Normal mode")
            print("Skill:", self.getskill())
        else:
            self.setskill2("Borushiki mode")
            print("Skill:", self.getskill2())

objekBattle = Battle("Boruto", 100, 70)
objekBattle.transformskill()