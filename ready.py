from grid import SCREEN_WIDTH, SCREEN_HEIGHT, drawFrame
from PIL import Image, ImageDraw
import time
from off import off
import os

img = Image.open(os.path.join(os.path.dirname(__file__), "ready.png"))

def ready(queue):
    drawFrame(img.load())
    time.sleep(3)
    off(queue)

