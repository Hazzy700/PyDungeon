import math

class Stat():
    def __init__(self, BaseValue, Add=1, Mul=1):
        self.Value = BaseValue
        self.Adds = {"Base" : Add}
        self.Multipliers = {"Base" : Mul}
        self.Random = {"Base" : 0}
    
    def GetIncrementAmount(self, amount=1):
        TotalAdd = 0
        for k, v in self.Adds.items():
            TotalAdd += v
        
        TotalMultiplier = 1
        for k, v in self.Multipliers.items():
            TotalMultiplier *= v

        return TotalAdd * TotalMultiplier * amount

    def Increment(self, amount):
        self.Value += self.GetIncrementAmount() * amount

    def GetLevel(self):
        xp = self.Value

        if xp < 10:
            level = 0
            current_threshold = 0
            next_threshold = 10
            return level, current_threshold, next_threshold - xp

        level = 0
        current_threshold = 10 
        next_level = 1

        while True:
            next_threshold = 10 + 5 * next_level * (next_level + 1)
            if next_threshold > xp:
                break
            current_threshold = next_threshold
            level = next_level
            next_level += 1

        to_next = next_threshold - xp

        return level, current_threshold, to_next

def UpdatePlayerGameState(gameState):
    level, _, _ = gameState["Exp"].GetLevel()
    gameState["Damage"].Adds["Level"] = level
    gameState["MaxHealth"].Adds["Level"] = level * 5

    if gameState["Gold"].Value <= 0:
        gameState["Gold"].Value = 0

    if gameState["CurrentState"] == "Menu":
        gameState["Health"].Value = gameState["MaxHealth"].GetIncrementAmount()
