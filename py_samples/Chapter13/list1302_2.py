class GameCharacter:
    def __init__(self, job, life):
        self.job = job
        self.life = life

warrior = GameCharacter("戰士", 100)
print(warrior.job)
print(warrior.life)
