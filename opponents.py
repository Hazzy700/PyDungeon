
from stats import Stat
from commands import Command, Commands

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

        self.Command = Command()
        self.Command.displayName = displayName
        self.Command.name = name
        self.Command.isEnabled = CanAttack
        self.Command.Run = self.Chosen

        Commands[displayName] = self.Command
    
    def Chosen(self, gameState):
        gameState["CurrentState"] = "Attacking"
        gameState["CurrentOpponent"] = self.name

    def Attack(self, gameState):
        damage = self.damage.GetIncrementAmount()
        gameState["Health"].Increment(-damage)
        print(self.displayName + " hit you for " + damage + " damage!")

    def TakeDamage(self, gameState):
        damage = gameState["Damage"].GetIncrementAmount()
        self.hp.Increment(-damage)
        print(self.displayName + " was damaged for " + damage + " damage!")


Opponents = {}

Opponents["slime"] = Opponent("slime", "Slime", 8, 1)