from PIL import Image, ImageDraw, ImageFont, ImageColor
from grid import LED_WIDTH, LED_HEIGHT, loopFrames

fnt = ImageFont.truetype("Roboto-Medium.ttf", 140)

frames = []
for i in range(1000):
    im = Image.new("RGB", (LED_WIDTH * 8, LED_HEIGHT * 8))
    draw = ImageDraw.Draw(im)
    fill = ImageColor.getrgb("hsv(" + str(i % 360) + ",100%,100%)")
    draw.text((200 - i, 0), "Hello, World!", font=fnt, fill=fill)
    im = im.resize((LED_WIDTH, LED_HEIGHT), Image.BICUBIC)
    px = im.load()
    frames.append(px)

loopFrames(frames, 0)
