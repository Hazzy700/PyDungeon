from opponents import Opponents

SCREEN_WIDTH = 120

PyDungeonAscii = """
   ▄███████▄ ▄██   ▄   ████████▄  ███    █▄  ███▄▄▄▄      ▄██████▄     ▄████████  ▄██████▄  ███▄▄▄▄  
  ███    ███ ███   ██▄ ███   ▀███ ███    ███ ███▀▀▀██▄   ███    ███   ███    ███ ███    ███ ███▀▀▀██▄
  ███    ███ ███▄▄▄███ ███    ███ ███    ███ ███   ███   ███    █▀    ███    █▀  ███    ███ ███   ███
  ███    ███ ▀▀▀▀▀▀███ ███    ███ ███    ███ ███   ███  ▄███         ▄███▄▄▄     ███    ███ ███   ███
▀█████████▀  ▄██   ███ ███    ███ ███    ███ ███   ███ ▀▀███ ████▄  ▀▀███▀▀▀     ███    ███ ███   ███
  ███        ███   ███ ███    ███ ███    ███ ███   ███   ███    ███   ███    █▄  ███    ███ ███   ███
  ███        ███   ███ ███   ▄███ ███    ███ ███   ███   ███    ███   ███    ███ ███    ███ ███   ███
 ▄████▀       ▀█████▀  ████████▀  ████████▀   ▀█   █▀    ████████▀    ██████████  ▀██████▀   ▀█   █▀ 
 ____________________________________________________________________________________________________
 ████████████████████████████████████████████████████████████████████████████████████████████████████
"""

AttackAscii = """
░▀▄░░▀▄░░░░█▀█░▀█▀░▀█▀░█▀█░█▀▀░█░█░░░░▄▀░░▄▀
░░▄▀░░▄▀░░░█▀█░░█░░░█░░█▀█░█░░░█▀▄░░░▀▄░░▀▄░
░▀░░░▀░░░░░▀░▀░░▀░░░▀░░▀░▀░▀▀▀░▀░▀░░░░░▀░░░▀
"""
ExitAscii = """
░▀▄░░▀▄░░░░█▀▀░█░█░▀█▀░▀█▀░░░░▄▀░░▄▀
░░▄▀░░▄▀░░░█▀▀░▄▀▄░░█░░░█░░░░▀▄░░▀▄░
░▀░░░▀░░░░░▀▀▀░▀░▀░▀▀▀░░▀░░░░░░▀░░░▀
"""

ChooseYourAscii = """
░█▀▀░█░█░█▀█░█▀█░█▀▀░█▀▀░░░█░█░█▀█░█░█░█▀▄
░█░░░█▀█░█░█░█░█░▀▀█░█▀▀░░░░█░░█░█░█░█░█▀▄
░▀▀▀░▀░▀░▀▀▀░▀▀▀░▀▀▀░▀▀▀░░░░▀░░▀▀▀░▀▀▀░▀░▀
"""
OpponentAscii = """
░█▀█░█▀█░█▀█░█▀█░█▀█░█▀▀░█▀█░▀█▀
░█░█░█▀▀░█▀▀░█░█░█░█░█▀▀░█░█░░█░
░▀▀▀░▀░░░▀░░░▀▀▀░▀░▀░▀▀▀░▀░▀░░▀░
"""

AttackingAscii = """
░█▀█░▀█▀░▀█▀░█▀█░█▀▀░█░█░▀█▀░█▀█░█▀▀ 
░█▀█░░█░░░█░░█▀█░█░░░█▀▄░░█░░█░█░█░█░
░▀░▀░░▀░░░▀░░▀░▀░▀▀▀░▀░▀░▀▀▀░▀░▀░▀▀▀░
"""

def PrintAsciiCentered(ascii_art: str):
    for line in ascii_art.splitlines():
        print(line.center(SCREEN_WIDTH))

def PrintCenter(toPrint):
    print(toPrint.center(SCREEN_WIDTH))

def Space(Height):
    print("\n" * Height, end="")

def LevelMessage(gameState):
    Level, Exp, ToNext = gameState["Exp"].GetLevel()
    LevelMessage : str = "Level: " + str(Level) + "." + " To next level: " + str(ToNext) + " Exp"
    print(LevelMessage.center(SCREEN_WIDTH))

def HealthDisplay(gameState):
    print(f"Current Health: {str(gameState["Health"].Value)}/{str(gameState["MaxHealth"].GetIncrementAmount())}".center(SCREEN_WIDTH))

def DisplayStats(gameState):
    LevelMessage(gameState)
    HealthDisplay(gameState)

def MenuButtons():
    PrintAsciiCentered(AttackAscii)
    Space(1)
    PrintAsciiCentered(ExitAscii)

def Menu(gameState):
    PrintAsciiCentered(PyDungeonAscii)
    Space(5)
    DisplayStats(gameState)
    Space(3)
    MenuButtons()

def AttackChoice(gameState):
    PrintAsciiCentered(ChooseYourAscii)
    PrintAsciiCentered(OpponentAscii)
    Space(5)

    for k, v in Opponents.items():
        opponentDisplay = v.displayName + ": " + str(v.maxHp.GetIncrementAmount()) + " HP"
        PrintCenter(opponentDisplay)
        Space(1)

def Attacking(gameState):
    PrintAsciiCentered(AttackingAscii)
    Space(1)
    PrintCenter(gameState["CurrentOpponent"])

def Render(gameState):
    Space(10)
    if gameState["CurrentState"] == "Menu":
        Menu(gameState)
    elif gameState["CurrentState"] == "AttackChoice":
        AttackChoice(gameState)
    elif gameState["CurrentState"] == "Attacking":
        Attacking(gameState)
 