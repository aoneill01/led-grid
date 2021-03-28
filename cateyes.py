import time
from grid import loadFrames, drawFrame

def cat_eyes(queue):
    frames = loadFrames('./cateyes/*.png')
    frame = 0
    while queue.empty():
        drawFrame(frames[frame])
        frame = (frame + 1) % len(frames)
        time.sleep(0.07)
    queue.get()
