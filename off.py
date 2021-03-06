from rpi_ws281x import Color
from grid import LED_WIDTH, LED_HEIGHT, strip

def off(queue):
    for i in range(LED_WIDTH * LED_HEIGHT): strip.setPixelColor(i, Color(0, 0, 0))
    strip.show()
    queue.get()

