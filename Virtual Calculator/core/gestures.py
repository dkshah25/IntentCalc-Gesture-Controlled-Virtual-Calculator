import math
import time

class GestureEngine:
    def __init__(self):
        self.pinched = False
        self.confirm_time = None

        self.prev_x = None
        self.swipe_time = None

    def distance(self, p1, p2):
        return math.hypot(p2[0]-p1[0], p2[1]-p1[1])

    def is_pinch(self, lm):
        return self.distance(lm[4], lm[8]) < 35

    def is_fist(self, lm):
        # Fingertips close to palm
        palm = lm[0]
        tips = [lm[i] for i in [8, 12, 16, 20]]
        return all(self.distance(palm, tip) < 60 for tip in tips)

    def interpret(self, lm):
        now = time.time()
        x, _ = lm[8]

        # ---------- PINCH (CLICK) ----------
        pinching = self.is_pinch(lm)

        if pinching and not self.pinched:
            self.pinched = True
            self.confirm_time = now
            return None

        if pinching and self.pinched:
            if now - self.confirm_time > 0.15:
                return "PRESS"

        if not pinching:
            self.pinched = False
            self.confirm_time = None

        # ---------- SWIPE LEFT (BACKSPACE) ----------
        if self.prev_x is not None:
            dx = x - self.prev_x
            if dx < -40:  # fast left movement
                self.prev_x = x
                return "BACKSPACE"

        self.prev_x = x

        # ---------- CLOSED FIST (CLEAR) ----------
        if self.is_fist(lm):
            if self.swipe_time is None:
                self.swipe_time = now
            elif now - self.swipe_time > 0.6:
                return "CLEAR"
        else:
            self.swipe_time = None

        return None
