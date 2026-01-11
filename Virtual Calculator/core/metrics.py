import time

class Metrics:
    def __init__(self):
        self.start = time.time()
        self.frames = 0

    def fps(self):
        self.frames += 1
        elapsed = time.time() - self.start
        return int(self.frames / elapsed) if elapsed > 0 else 0
