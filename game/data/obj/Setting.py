class set():
    def __init__(self):
        self.width=1920
        self.height=1080
        self.size=40
        self.FPS = 60
        self.Fall_speed=4
        self.wall=None
        self.time_adjustment=60/self.FPS
        self.MAX_SPEED = 3*self.time_adjustment  # 최대 속도

    def set_FPS(self,FPS):
        self.FPS=FPS
        self.time_adjustment=60/self.FPS
        self.MAX_SPEED=3*self.time_adjustment

setting=set()