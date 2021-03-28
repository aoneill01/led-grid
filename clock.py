from grid import SCREEN_WIDTH, SCREEN_HEIGHT, drawFrame
from PIL import Image, ImageDraw
from datetime import datetime
import time
import os

sprites = Image.open(os.path.join(os.path.dirname(__file__), "IBM_PC_V3_8x8.png"))
def get_sprite(row, col):
    return sprites.crop((col * 9, row * 9, (col + 1) * 9 - 1, (row + 1) * 9 - 1))

def get_num(num):
    return get_sprite(3, num)

dark = Image.new("RGB", (52, 20))
dark.paste((0, 0, 0), [0,0,dark.size[0],dark.size[1]])

light = Image.new("RGB", (52, 20))
light.paste((25, 189, 0), [0,0,light.size[0],light.size[1]])
draw = ImageDraw.Draw(light)
# for row in range(0, 20, 2):
    # draw.line([(0, row), (52, row)], fill = (21, 155, 0), width = 0)
    # draw.line([(0, row), (52, row)], fill = (7, 47, 0), width = 0)

mask = Image.new("L", (52, 20))

def draw(show_cursor):
    now = datetime.now()
    mask.paste((0), [0,0,mask.size[0],mask.size[1]])

    # mask.paste(get_num(now.month // 10), (0, 3))
    # mask.paste(get_num(now.month % 10), (8, 3))
    # mask.paste(get_sprite(2, 15), (16, 3))
    mask.paste(get_sprite(4, 13), (0, 3))
    mask.paste(get_sprite(6, 1), (8, 3))
    mask.paste(get_sprite(7, 2), (16, 3))
    mask.paste(get_num(now.day // 10), (0, 11))
    mask.paste(get_num(now.day % 10), (8, 11))

    mask.paste(get_num(now.hour // 10), (28, 3))
    mask.paste(get_num(now.hour % 10), (36, 3))
    mask.paste(get_sprite(3, 10), (44, 3))
    mask.paste(get_num(now.minute // 10), (28, 11))
    mask.paste(get_num(now.minute % 10), (36, 11))
    if show_cursor: mask.paste(get_sprite(1, 6), (44, 11))

def clock(queue):
    i = 0
    while queue.empty():
        draw(i % 2 == 0)
        # for row in range(0, 20, 2):
        #     if i % 2 == 0: draw.line([(0, row), (52, row)], fill = (21, 155, 0), width = 0)
        #     else: draw.line([(0, row), (52, row)], fill = (11, 80, 0), width = 0)
        im = Image.composite(light, dark, mask)
        drawFrame(im.load())
        time.sleep(1)
        i += 1
    queue.get()

