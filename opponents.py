
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

Opponents["slime"] = Opponent("slime", "Slime", 8, 1)