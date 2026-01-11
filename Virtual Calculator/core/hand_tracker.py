import mediapipe as mp
import cv2

class HandTracker:
    def __init__(self):
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(
            max_num_hands=1,
            min_detection_confidence=0.7,
            min_tracking_confidence=0.7
        )
        self.drawer = mp.solutions.drawing_utils

    def get_landmarks(self, frame):
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.hands.process(rgb)

        if not results.multi_hand_landmarks:
            return None

        hand = results.multi_hand_landmarks[0]
        h, w, _ = frame.shape
        lm = [(int(p.x * w), int(p.y * h)) for p in hand.landmark]

        self.drawer.draw_landmarks(frame, hand, self.mpHands.HAND_CONNECTIONS)
        return lm