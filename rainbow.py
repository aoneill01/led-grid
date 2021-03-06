import time
from rpi_ws281x import Color
from grid import LED_WIDTH, LED_HEIGHT, strip

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

def rainbow(queue):
    count = 0.0
    while queue.empty():
        for x in range(LED_WIDTH):
            for y in range(LED_HEIGHT):
                setPixel(strip, x, y, hsv_to_color((count + x + y) / 20, 1, 1))
        count += 0.3
        strip.show()
    queue.get()
