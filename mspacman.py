from grid import LED_WIDTH, LED_HEIGHT, drawFrame
from PIL import Image, ImageDraw
import time

sprites = Image.open("sprites.png")
def get_sprite(row, col):
    return sprites.crop((col * 20 + 6, row * 20 + 6, col * 20 + 6 + 16, row * 20 + 6 + 16))

im = Image.new("RGB", (LED_WIDTH, LED_HEIGHT))
draw = ImageDraw.Draw(im)

def draw_ms_pacman(i):
    lookup = [6, 6, 4, 4, 5, 5, 4, 4]
    t = i % 300
    if t < 150:
        x = LED_WIDTH - t
        im.paste(get_sprite(0, lookup[i % len(lookup)]), (x, 2))
    else:
        t -= 150
        x = t - 16 - 16 * 4
        im.paste(get_sprite(1, lookup[i % len(lookup)]), (x, 2))

def draw_ghost(i, ghost_num):
    t = i % 300
    if t < 150:
        lookup = [4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5]
        x = LED_WIDTH - t + 32 + 16 * ghost_num
        im.paste(get_sprite(4 + ghost_num, lookup[i % len(lookup)]), (x, 2))
    else:
        lookup = [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1]
        t -= 150
        x = t - 16 - 16 * ghost_num
        im.paste(get_sprite(8, lookup[i % len(lookup)]), (x, 2))

def ms_pacman(queue):
    i = 0
    while queue.empty():
        draw.rectangle((0, 0, LED_WIDTH, LED_HEIGHT), fill=(0, 0, 0))
        draw_ms_pacman(i)
        draw_ghost(i, 0)
        draw_ghost(i, 1)
        draw_ghost(i, 2)
        draw_ghost(i, 3)
        drawFrame(im.load())
        i += 1
        time.sleep(0.03)
    queue.get()
