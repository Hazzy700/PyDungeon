
from commands import resolveCommand
from globals import PrintAsciiCentered, PrintCenter, Space, Opponents, Commands
from stats import Stat, UpdatePlayerGameState
from render import Render
from opponents import Opponent
from commands import Command

def GameLoop():
    gameState = {
        # States
        "CurrentState" : "Menu",
        "Exit" : False,

        "CurrentOpponent" : "",

        # Stats
        "Health" : Stat(10),
        "MaxHealth" : Stat(0, 10),
        "Damage" : Stat(0),
        "TimingBonus" : Stat(0, 1.25),
        "MissedReduction" : Stat(0, 0.8),

        "Exp" : Stat(0)
    }

    Render(gameState)
    UpdatePlayerGameState(gameState)

    while not gameState["Exit"]:
        Space(5)
        inp = input("> ")
        command = resolveCommand(inp, gameState)
        if isinstance(command, str):
            print(command)
        else:
            if command.isEnabled(gameState):
                command.Run(gameState)
                if command.triggersRender:
                    Render(gameState)
            

GameLoop()