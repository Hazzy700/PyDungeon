
from commands import Commands, resolveCommand
from render import Render
from stats import Stat


def GameLoop():
    gameState = {
        # States
        "CurrentState" : "Menu",
        "Exit" : False,

        # Stats
        "Health" : Stat(10),
        "MaxHealth" : Stat(0, 10),
        "Damage" : Stat(0),
        "TimingBonus" : Stat(0, 1.25),

        "Exp" : Stat(1)
    }

    Render(gameState)
    while not gameState["Exit"]:
        inp = input("> ")
        command = resolveCommand(inp)
        if isinstance(command, str):
            print(command)
        else:
            if command.isEnabled(gameState):
                command.Run(gameState)
                if command.triggersRender:
                    Render(gameState)
            

GameLoop()