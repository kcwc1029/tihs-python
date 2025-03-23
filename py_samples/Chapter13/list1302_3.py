class GameCharacter:
    def __init__(self, job, life):
        self.job = job
        self.life = life

    def info(self):
        print(self.job)
        print(self.life)

warrior = GameCharacter("戰士", 100)
warrior.info()
