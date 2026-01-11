import cv2

class HUD:
    def __init__(self):
        self.buttons = []
        self.layout = [
            ["7","8","9","/"],
            ["4","5","6","*"],
            ["1","2","3","-"],
            ["0",".","=","+"]
        ]

        start_x, start_y = 120, 200
        gap_x, gap_y = 120, 95

        for r in range(4):
            for c in range(4):
                self.buttons.append({
                    "text": self.layout[r][c],
                    "pos": (start_x + c*gap_x, start_y + r*gap_y),
                    "size": (95, 75)
                })

    def draw_glass_button(self, frame, btn, intensity=0.25):
        x,y = btn["pos"]
        w,h = btn["size"]

        overlay = frame.copy()

        # Operator color coding
        if btn["text"] in "+-*/=":
            color = (0, 220, 255)   # cyan
        else:
            color = (160, 160, 160) # neutral

        cv2.rectangle(overlay,(x,y),(x+w,y+h),color,-1)
        cv2.addWeighted(overlay,intensity,frame,1-intensity,0,frame)

        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,255,255),1)

        cv2.putText(frame,btn["text"],
                    (x+28,y+50),
                    cv2.FONT_HERSHEY_DUPLEX,
                    1.6,(255,255,255),2)

    def render(self, frame, hover=None):
        for btn in self.buttons:
            if btn == hover:
                self.draw_glass_button(frame, btn, intensity=0.45)
            else:
                self.draw_glass_button(frame, btn, intensity=0.22)

    def get_hover(self, x, y):
        for btn in self.buttons:
            bx,by = btn["pos"]
            bw,bh = btn["size"]
            if bx < x < bx+bw and by < y < by+bh:
                return btn
        return None

    def draw_display(self, frame, text):
        overlay = frame.copy()
        cv2.rectangle(overlay,(90,90),(650,160),(30,30,30),-1)
        cv2.addWeighted(overlay,0.6,frame,0.4,0,frame)

        cv2.rectangle(frame,(90,90),(650,160),(0,255,255),2)

        cv2.putText(frame,text,
                    (110,145),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    2.2,(0,255,255),3)
