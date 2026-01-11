import cv2
from core.hand_tracker import HandTracker
from core.gestures import GestureEngine
from core.ui import HUD
from core.calculator import CalculatorEngine
from core.metrics import Metrics
last_press_time = 0

cap = cv2.VideoCapture(0)
cap.set(3,1280)
cap.set(4,720)

tracker = HandTracker()
gesture = GestureEngine()
ui = HUD()
calc = CalculatorEngine()
metrics = Metrics()

prev_tip = None

while True:
    _, frame = cap.read()
    frame = cv2.flip(frame,1)

    lm = tracker.get_landmarks(frame)
    hover = None

    if lm:
        x,y = lm[8]
        hover = ui.get_hover(x,y)
        action = gesture.interpret(lm)
        prev_tip = (x,y)

        import time
        now = time.time()
        if action == "PRESS" and hover:
            if now - last_press_time > 0.25:
                last_press_time = now

            if hover["text"] == "=":
                calc.expr = calc.evaluate()
            else:
                calc.input(hover["text"])

        elif action == "BACKSPACE":
            if now - last_press_time > 0.25:
                last_press_time = now
                calc.backspace()

        elif action == "CLEAR":
            if now - last_press_time > 0.6:
                last_press_time = now
                calc.clear()

    ui.draw_display(frame, calc.expr)
    ui.render(frame, hover)


    cv2.putText(frame,f"FPS: {metrics.fps()}",
                (1100,40),cv2.FONT_HERSHEY_PLAIN,2,(0,255,0),2)

    cv2.imshow("Dharmit Shah & Ishaan Chand | Virtual Calculator", frame)
    if cv2.waitKey(1)==27:
        break

cap.release()
cv2.destroyAllWindows()