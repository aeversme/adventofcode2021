class Player:
    def __init__(self, name, start):
        self.name = name
        self.space = start
        self.score = 0
        self.victories = 0

    def __repr__(self):
        return f"{self.name} on {self.space} with {self.score} points"
