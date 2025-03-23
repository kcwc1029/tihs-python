class Human:
    def __init__(self, name, life):
        self.name = name
        self.life = life

    def info(self):
        print(self.name)
        print(self.life)


class Soldier(Human):
    def __init__(self, name, life, weapon):
        super().__init__(name, life)
        self.weapon = weapon

    def info(self):
        print("我的名字是"+self.name)
        print("我的體力{}".format(self.life))

    def talk(self):
        print("帶著" + self.weapon + "踏上冒險的旅程")


man = Human("托姆(村民)", 50)
man.info()
print("----------")
prince = Soldier("阿克雷思(王子)", 200, "光之劍")
prince.info()
prince.talk()
