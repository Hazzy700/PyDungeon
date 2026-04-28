SCREEN_WIDTH = 120

Opponents = {}
Commands = {}

def PrintAsciiCentered(ascii_art: str):
    for line in ascii_art.splitlines():
        print(line.center(SCREEN_WIDTH))

def PrintCenter(toPrint):
    print(toPrint.center(SCREEN_WIDTH))

def Space(Height):
    print("\n" * Height, end="")