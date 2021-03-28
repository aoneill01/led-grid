import time
from grid import loadFrames, drawFrame

def bright_eyes(queue):
    frames = loadFrames('./brighteyes/*.png')
    frame = 0
    while queue.empty():
        drawFrame(frames[frame])
        frame = (frame + 1) % len(frames)
        time.sleep(0.07)
    queue.get()
