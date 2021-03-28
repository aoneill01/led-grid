from PIL import Image, ImageDraw, ImageFont, ImageColor
from grid import SCREEN_WIDTH, SCREEN_HEIGHT, drawFrame

multiplier = 4
fnt = ImageFont.truetype("Roboto-Thin.ttf", 70)

def text(queue):
    text = queue.get()
    fill = ImageColor.getrgb(queue.get())
     
    (width, height) = fnt.getsize(text)
     
    frames = []
    for i in range(SCREEN_WIDTH * multiplier + width):
        im = Image.new("RGB", (SCREEN_WIDTH * multiplier, SCREEN_HEIGHT * multiplier))
        draw = ImageDraw.Draw(im)
        draw.text((SCREEN_WIDTH * multiplier - i, 0), text, font=fnt, fill=fill)
        im = im.resize((SCREEN_WIDTH, SCREEN_HEIGHT), Image.BICUBIC)
        px = im.load()
        frames.append(px)

    frame = 0
    while queue.empty():
        drawFrame(frames[frame % len(frames)])
        frame += 1

    queue.get()
