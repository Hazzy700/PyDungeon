
from commands import Commands, resolveCommand
from render import Render


def GameLoop():
    gameState = {"CurrentState" : "Menu", "Exit" : False}

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