import time
from PIL import Image
from rpi_ws281x import PixelStrip, Color

LED_WIDTH = 24
LED_HEIGHT = 20
LED_PIN = 18          # GPIO pin connected to the pixels (18 uses PWM!).
LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA = 10          # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255  # Set to 0 for darkest and 255 for brightest
LED_INVERT = False    # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53

def drawFrame(px):
    x = LED_WIDTH - 1
    y = LED_HEIGHT - 1
    dy = -1
    i = 0
    while x >= 0:
        (r, g, b) = px[x, y]
        color = Color(r, g, b)
        strip.setPixelColor(i, color)
        i += 1
        y += dy
        if y < 0 or y >= LED_HEIGHT:
            dy *= -1
            y += dy
            x -= 1

    strip.show()

frames = Image.open("cat.gif").n_frames
print(frames)
im = Image.open("cat.gif")
p = im.getpalette()
im.seek(0)
n = im.convert("RGBA")
im.seek(1)
im.putpalette(p)
n.paste(im, (0, 0), im.convert("RGBA"))

n.show()
# px = im.convert("RGBA").load()
# print(px[0, 0])
# im.seek(5)
# px = im.convert("RGBA").load()
# print(px[0, 0])
# for f in range(0, frames):
#     im.seek(f)
#     px = im.convert("RGBA").load()
#     print(px[0, 0])

# strip = PixelStrip(LED_WIDTH * LED_HEIGHT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
# strip.begin()

# frame = 0
# while True:
#     px = im.convert("RGB").load()
#     drawFrame(px)
#     frame = (frame + 1) % 93
#     time.sleep(.1)