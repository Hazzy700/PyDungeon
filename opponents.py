
from stats import Stat
from commands import Command
from globals import PrintAsciiCentered, PrintCenter, Space, Opponents, Commands

def CanAttack(gameState):
    return gameState["CurrentState"] == "AttackChoice"

class Opponent():
    def __init__(self, name, displayName, maxHp, damage):
        self.name = name
        self.displayName = displayName
        self.damage = Stat(0, damage)
        self.maxHp = Stat(0, maxHp)
        self.hp = Stat(maxHp)
        self.critChance = Stat(0, 10)
        self.critDamage = Stat(0, 1.25)
        self.AwardMultiplier = Stat(0)

        self.Command = Command()
        self.Command.displayName = displayName
        self.Command.description = "Attack a " + displayName
        self.Command.name = name
        self.Command.isEnabled = CanAttack
        self.Command.Run = self.Chosen

        Commands[displayName] = self.Command
    
    def Chosen(self, gameState):
        gameState["CurrentState"] = "Attacking"
        gameState["CurrentOpponent"] = self.name
        self.hp.Value = self.maxHp.GetIncrementAmount()
        PrintCenter(str(self.hp.Value))

    def Attack(self, gameState):
        damage = self.damage.GetIncrementAmount()
        gameState["Health"].Increment(-damage)
        PrintCenter(self.displayName + " hit you for " + str(damage) + " damage!")

    def TakeDamage(self, gameState, Multiplier):
        damage = gameState["Damage"].GetIncrementAmount() * Multiplier
        self.hp.Increment(-damage)
        PrintCenter(self.displayName + " was damaged for " + str(damage) + " damage!")

    def Death(self, gameState):
        xpAwarded = self.maxHp.GetIncrementAmount() * self.damage.GetIncrementAmount() * self.AwardMultiplier.GetIncrementAmount()
        gameState["Exp"].Increment(xpAwarded)
        gameState["Gold"].Increment(xpAwarded * 0.4)
        PrintCenter(self.displayName + " died and awarded you " + str(gameState["Exp"].GetIncrementAmount(xpAwarded)) + " Exp and " + str(gameState["Gold"].GetIncrementAmount(xpAwarded * 0.4)) + " Gold!")
    
    def EnemyWin(self, gameState):
        goldTook = round(self.maxHp.GetIncrementAmount() * self.damage.GetIncrementAmount() * 0.1)
        gameState["Gold"].Increment(goldTook)
        PrintCenter(self.displayName + " has killed you! You lost " + str(gameState["Gold"].GetIncrementAmount(goldTook)))

Opponents["slime"] = Opponent("slime", "Slime", 8, 1)
Opponents["zombie"] = Opponent("zombie", "Zombie", 22, 3)
Opponents["skeleton"] = Opponent("skeleton", "Skeleton", 40, 3.5)
Opponents["spider"] = Opponent("spider", "Spider", 55, 6.5)
Opponents["corruptor"] = Opponent("corruptor", "Corruptor", 120, 6)
Opponents["Sam the MOUNTAIN"] = Opponent("Sam the MOUNTAIN", "Sam the MOUNTAIN", 10_000, 45)
Opponents["Luke is CROSS"] = Opponent("Luke is CROSS", "Luke is CROSS", 25_000, 90)
Opponents["Raffy P"] = Opponent("Raffy P", "Raffy P", 50_000, 365)