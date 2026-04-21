class Command():
    def __init__(self):
        self.displayName = "unset"
        self.name = ""
        self.description = ""
        self.triggersRender = True

    def isEnabled(self, gameState):
        return True

    def Run(self):
        return True

Commands = {} 

def indexCommand(ToIndex : Command):
    Commands[ToIndex.name] = ToIndex

# Help

help = Command()
help.name = "help"
help.displayName = "Help"
help.description = "Display currently available commands"
help.triggersRender = False

def helpRun(gameState):
    for k, v in Commands.items():
        if not v.isEnabled(gameState):
            continue
        print(">> " + v.displayName + ": " + v.description)

help.Run = helpRun

indexCommand(help)

# Attack

attack = Command()
attack.name = "attack"
attack.displayName = "Attack"
attack.description = "Start an attack on an opponent"
attack.triggersRender = True

def attackRun(gameState):
    gameState["CurrentState"] = "AttackChoice"

def attackIsEnabled(gameState):
    if gameState["CurrentState"] == "Menu":
        return True
    return False

attack.Run = attackRun
attack.isEnabled = attackIsEnabled

indexCommand(attack)

# exit

exit = Command()
exit.name = "exit"
exit.displayName = "Exit"
exit.description = "Exits the game loop"
exit.triggersRender = False

def exitRun(gameState):
    gameState["Exit"] = True

exit.Run = exitRun

indexCommand(exit)

# Resolve Command

def resolveCommand(input_str: str):
    input_str = input_str.lower()

    # Step 1: find all commands whose names start with the input
    matches = [cmd for name, cmd in Commands.items()
               if name.lower().startswith(input_str)]

    if len(matches) == 0:
        return "No matches to command"  # no command matches

    if len(matches) == 1:
        return matches[0]  # unique match

    return "Ambiguous search"