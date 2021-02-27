from grid import LED_WIDTH, LED_HEIGHT, drawFrame
from PIL import Image, ImageDraw
import time

sprites = Image.open("sprites.png")
def getSprite(row, col):
    return sprites.crop((col * 20 + 6, row * 20 + 6, col * 20 + 6 + 16, row * 20 + 6 + 16))

im = Image.new("RGB", (LED_WIDTH, LED_HEIGHT))
draw = ImageDraw.Draw(im)

def drawMsPacman(i):
    lookup = [6, 6, 4, 4, 5, 5, 4, 4]
    x = LED_WIDTH - ((1 * i) % 150)
    im.paste(getSprite(0, lookup[i % len(lookup)]), (x, 2))

def drawGhost(i, ghostNum):
    lookup = [4, 4, 4, 4, 5, 5, 5, 5]
    x = LED_WIDTH - ((1 * i) % 150) + 24 + 16 * ghostNum
    im.paste(getSprite(4 + ghostNum, lookup[i % len(lookup)]), (x, 2))

i = 0
while True:
    draw.rectangle((0, 0, LED_WIDTH, LED_HEIGHT), fill=(0, 0, 0))
    drawMsPacman(i)
    drawGhost(i, 0)
    drawGhost(i, 1)
    drawGhost(i, 2)
    drawGhost(i, 3)
    drawFrame(im.load())
    i += 1
    time.sleep(0.05)
