from grid import SCREEN_WIDTH, SCREEN_HEIGHT, drawFrame
from PIL import Image, ImageDraw
from datetime import datetime
import time
import os

sprites = Image.open(os.path.join(os.path.dirname(__file__), "IBM_PC_V3_8x8.png"))

background = Image.new("RGB", (52, 20))
background.paste((0, 0, 0), [0,0,background.size[0],background.size[1]])

foreground = Image.new("RGB", (52, 20))
foreground.paste((25, 189, 0), [0,0,foreground.size[0],foreground.size[1]])

mask = Image.new("L", (52, 20))

def get_sprite(row, col):
    return sprites.crop((col * 9, row * 9, (col + 1) * 9 - 1, (row + 1) * 9 - 1))

def get_char(c):
    order = ord(c)
    return get_sprite(order // 16, order % 16)

def get_output(phrase):
    row1 = 2
    row2 = 11
    positions = [(0, row1), (8, row1), (16, row1), (0, row2), (8, row2), (16, row2), (28, row1), (36, row1), (44, row1), (28, row2), (36, row2), (44, row2)]
    return zip(positions, map(get_char, phrase))

def format_clock_string(i):
    now = datetime.now()
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    time_separators = [" ", ":"]
    am_pm_indicator = " "
    hour = now.hour
    if hour > 12:
        am_pm_indicator = "."
        hour -= 12
    return f"{months[now.month - 1]}/{now.day:02d}{hour:02d}{time_separators[i % 2]}{now.minute:02d}{am_pm_indicator}"

def clock(queue):
    i = 0
    while queue.empty():
        mask.paste((0), [0,0,mask.size[0],mask.size[1]])
        for position, sprite in get_output(format_clock_string(i)):
            mask.paste(sprite, position)
        im = Image.composite(foreground, background, mask)
        drawFrame(im.load())
        time.sleep(1)
        i += 1
    queue.get()

