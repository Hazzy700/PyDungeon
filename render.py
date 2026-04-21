

def Render(gameState):
    if gameState["CurrentState"] == "Menu":
        print("menu")
    elif gameState["CurrentState"] == "AttackChoice":
        print("Attack choice")