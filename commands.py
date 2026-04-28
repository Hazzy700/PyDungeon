from globals import PrintAsciiCentered, PrintCenter, Space, Opponents, Commands
import time
import random

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

# hit

hit = Command()
hit.name = "hit"
hit.displayName = "Hit"
hit.description = "hit and opponent"
hit.triggersRender = True

def hitRun(gameState):
    Space(2)
    PrintCenter("Hit enter as soon as you see the word 'HIT'! for a critical hit bonus.")
    PrintCenter("Press enter when you are ready.")
    input("")

    Opponent = Opponents[gameState["CurrentOpponent"]]

    done = False
    chance = 0
    max = 10

    while not done:
        PrintCenter("...")
        time.sleep(0.5 + (random.randint(1,5) / 10))
        chance += 1
        done = random.randint(min(chance, max-1), max) == max-1

    PrintCenter("HIT")
    StartTime = time.time()
    input()
    EndTime = time.time()

    TimeElapsed = EndTime - StartTime
    if TimeElapsed < 0.5:
        PrintCenter("CRITICAL HIT!")
        Opponent.TakeDamage(gameState, gameState["TimingBonus"].GetIncrementAmount())
    elif TimeElapsed < 1:
        PrintCenter("Average hit")
        Opponent.TakeDamage(gameState, 1)
    else:
        PrintCenter("...Poor hit...")
        Opponent.TakeDamage(gameState, gameState["MissedReduction"].GetIncrementAmount())

    time.sleep(0.5)

    Space(2)

    if Opponent.hp.Value <= 0:
        gameState["CurrentState"] = "Menu"
        PrintCenter("You won!")
        return

    Opponent.Attack(gameState)
    time.sleep(0.5)

def hitIsEnabled(gameState):
    return gameState["CurrentState"] == "Attacking"

hit.Run = hitRun
hit.isEnabled = hitIsEnabled

indexCommand(hit)

# run

run = Command()
run.name = "run"
run.displayName = "Run"
run.description = "Run from battle"

def runRun(gameState):
    if random.randint(1,4) >= 2:
        gameState["CurrentState"] = "Menu"
        Space(3)
        PrintCenter("You ran...")
        Space(3)
    else:
        Space(3)
        PrintCenter("failed run!")

def runIsEnabled(gameState):
    return gameState == "Attacking"

run.Run = runRun
run.isEnabled = runIsEnabled

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

def resolveCommand(input_str: str, gameState):
    input_str = input_str.lower()

    # Step 1: find all commands whose names start with the input
    matches = [cmd for name, cmd in Commands.items()
               if name.lower().startswith(input_str) and cmd.isEnabled(gameState)]

    if len(matches) == 0:
        return "No matches to command"  # no command matches

    if len(matches) == 1:
        return matches[0]  # unique match

    return "Ambiguous search"