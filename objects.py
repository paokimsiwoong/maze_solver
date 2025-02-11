class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line():
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        # p1, p2는 Point 클래스

    
    # def draw(self, canvas, fill_color):
    def draw(self, canvas, fill_color="black"):
    # @@@ 해답처럼 fill_color 기본값 지정하기
        # canvas(tkinter.Canvas)를 받아서 그 canvas에 fill_color색 선을 그리는 함수
        canvas.create_line(self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill=fill_color, width=2)
        # p1, p2를 잇는 선 그리기