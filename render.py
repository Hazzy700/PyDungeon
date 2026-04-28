from globals import PrintAsciiCentered, PrintCenter, Space, Opponents, Commands

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

HitAscii = """
░▀▄░░▀▄░░░░█░█░▀█▀░▀█▀░░░░▄▀░░▄▀
░░▄▀░░▄▀░░░█▀█░░█░░░█░░░░▀▄░░▀▄░
░▀░░░▀░░░░░▀░▀░▀▀▀░░▀░░░░░░▀░░░▀
"""
RunAscii = """
░▀▄░░▀▄░░░░█▀▄░█░█░█▀█░░░░▄▀░░▄▀
░░▄▀░░▄▀░░░█▀▄░█░█░█░█░░░▀▄░░▀▄░
░▀░░░▀░░░░░▀░▀░▀▀▀░▀░▀░░░░░▀░░░▀
"""

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
    Space(2)
    Opponent = Opponents[gameState["CurrentOpponent"]]
    PrintCenter(Opponent.displayName)
    PrintCenter(f"{str(Opponent.hp.Value)}/{str(Opponent.maxHp.GetIncrementAmount())}HP")
    Space(1)
    HealthDisplay(gameState)
    Space(1)
    PrintAsciiCentered(HitAscii)
    Space(1)
    PrintAsciiCentered(RunAscii)

def Render(gameState):
    Space(10)
    if gameState["CurrentState"] == "Menu":
        Menu(gameState)
    elif gameState["CurrentState"] == "AttackChoice":
        AttackChoice(gameState)
    elif gameState["CurrentState"] == "Attacking":
        Attacking(gameState)
 