import time
from rpi_ws281x import PixelStrip, Color

# LED strip configuration:
LED_WIDTH = 24
LED_HEIGHT = 20
LED_PIN = 18          # GPIO pin connected to the pixels (18 uses PWM!).
LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA = 10          # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 16  # Set to 0 for darkest and 255 for brightest
LED_INVERT = False    # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53

def setPixel(strip, x, y, color):
    index = x * LED_HEIGHT + (y, LED_HEIGHT - y - 1)[x % 2 == 0]
    strip.setPixelColor(index, color)

def hsv_to_color(h, s, v):
    if s == 0.0: v*=255; return Color(v, v, v)
    i = int(h*6.) # XXX assume int() truncates!
    f = (h*6.)-i; p,q,t = int(255*(v*(1.-s))), int(255*(v*(1.-s*f))), int(255*(v*(1.-s*(1.-f)))); v*=255; i%=6
    if i == 0: return Color(v, t, p)
    if i == 1: return Color(q, v, p)
    if i == 2: return Color(p, v, t)
    if i == 3: return Color(p, q, v)
    if i == 4: return Color(t, p, v)
    if i == 5: return Color(v, p, q)

# Main program logic follows:
if __name__ == '__main__':
    # Create NeoPixel object with appropriate configuration.
    strip = PixelStrip(LED_WIDTH * LED_HEIGHT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
    # Intialize the library (must be called once before other functions).
    strip.begin()

    count = 0.0
    while True:
        for x in range(LED_WIDTH):
            for y in range(LED_HEIGHT):
                setPixel(strip, x, y, hsv_to_color((count + x + y) / 20, 1, 1))
        count += 0.1
        strip.show()
