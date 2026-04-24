import math

class Stat():
    def __init__(self, BaseValue, Add=1, Mul=1):
        self.Value = BaseValue
        self.Adds = {"Base" : Add}
        self.Multipliers = {"Base" : Mul}
    
    def GetIncrementAmount(self):
        TotalAdd = 0
        for k, v in self.Adds.items():
            TotalAdd += v
        
        TotalMultiplier = 1
        for k, v in self.Multipliers.items():
            TotalMultiplier *= v

        return TotalAdd * TotalMultiplier

    def Increment(self, amount):
        self.Value += self.GetIncrementAmount() * amount

    def GetLevel(self):
        xp = self.Value

        # Handle below first threshold
        if xp < 10:
            level = 0
            current_threshold = 0
            next_threshold = 10
            return level, current_threshold, next_threshold - xp

        level = 0
        current_threshold = 10  # a(0) if you like, or treat this as level 1 start
        next_level = 1

        # Walk upwards until the next level would exceed xp
        while True:
            next_threshold = 10 + 5 * next_level * (next_level + 1)
            if next_threshold > xp:
                break
            current_threshold = next_threshold
            level = next_level
            next_level += 1

        # Distance to next level
        to_next = next_threshold - xp

        return level, current_threshold, to_next
