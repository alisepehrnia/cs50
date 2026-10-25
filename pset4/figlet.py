import sys
from random import choice
from pyfiglet import Figlet

if len(sys.argv) != 1 and len(sys.argv) != 3:
    sys.exit("Incorrect arguments")

font = None
if len(sys.argv) == 3:
    if sys.argv[1] == "-f" or sys.argv[1] == "--font":
        font = sys.argv[2]
    else:
        sys.exit("Incorrect arguments")

figlet = Figlet()
fonts = figlet.getFonts()
if font != None and font not in fonts:
    sys.exit("Incorrect arguments")

if font == None:
    font = choice(figlet.getFonts())
figlet.setFont(font=font)

inp = input("Enter your text: ")

print(figlet.renderText(inp))